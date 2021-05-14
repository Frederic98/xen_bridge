import functools
import inspect
import typing
from datetime import tzinfo
from typing import Any
import datetime

import sys


class XenEndpoint:
    def __init__(self, connection):
        self.connection = connection
        if not hasattr(self, 'xenpath'):
            self.xenpath = self.__class__.__name__

    def call(self, methodname, *args):
        return self.connection.call(self.xenpath + '.' + methodname, *replace_xen_ref(args))

    def cast_xen_object(self, obj, hint):
        # ToDo: parse dict
        if typing.get_origin(hint) is list:
            hint_args = typing.get_args(hint)
            return [self.cast_xen_object(itm, hint_args[0]) for itm in obj]
        if typing.get_origin(hint) is tuple:
            hint_args = typing.get_args(hint)
            if hint_args[-1] is Ellipsis:
                hint_args = hint_args[:-1]
                hint_args += (hint_args[-1]) * (len(obj) - len(hint_args))
            return tuple(self.cast_xen_object(itm, hint) for itm, hint in zip(obj, hint_args))
        if inspect.isclass(hint) and issubclass(hint, XenObject):
            return hint(self.connection, obj)
        if hint is datetime.datetime:
            date = datetime.datetime.strptime(obj.value, '%Y%m%dT%H:%M:%SZ')
            return date.replace(tzinfo=datetime.timezone.utc)
        return obj


class XenObject(XenEndpoint):
    def __init__(self, connection, ref):
        XenEndpoint.__init__(self, connection)
        self.ref = ref

    def call(self, methodname, *args):
        return XenEndpoint.call(self, methodname, self, *args)      # Add object ref (self) to arguments


def XenMethod(func: typing.Callable = None, methodname: str = None, sig: inspect.Signature=None):
    if func is not None:
        methodname = func.__name__
        sig = inspect.signature(func)
    if methodname is None:
        raise ValueError('Either a reference function or function name should be given!')
    for arg in sig.parameters.values():
        if arg.kind in (inspect.Parameter.KEYWORD_ONLY, inspect.Parameter.VAR_KEYWORD):
            raise SystemError(f'Argument {arg.name} of function {methodname} is a keyword argument, which is not supported by XMLRPC')

    def wrapper(self: XenEndpoint, *args, **kwargs):
        arguments = sig.bind(self, *args, **kwargs)
        arguments.apply_defaults()
        arguments = arguments.args[1:]       # Remove 'self'
        result = self.call(methodname, *arguments)
        if sig.return_annotation is not inspect.Signature.empty:
            module_ns = sys.modules[self.__class__.__module__].__dict__
            result = self.cast_xen_object(result, typing.get_type_hints(getattr(self, methodname), module_ns).get('return'))
        return result

    if func is not None:
        wrapper = functools.wraps(func)(wrapper)       # Apply @functools.wraps(func) decorator
    else:
        wrapper.__name__ = methodname
        wrapper.__annotations__ = {}
        for arg in sig.parameters.values():
            if arg.annotation is not inspect.Parameter.empty:
                wrapper.__annotations__[arg.name] = arg.annotation
        if sig.return_annotation is not inspect.Signature.empty:
            wrapper.__annotations__['return'] = sig.return_annotation
        wrapper.__signature__ = sig
    return wrapper


def replace_xen_ref(value: Any):
    if isinstance(value, (list, tuple)):
        return [replace_xen_ref(itm) for itm in value]
    if isinstance(value, XenObject):
        return value.ref
    return value


class XenProperty:
    READONLY = 0b01
    WRITEONLY = 0b10
    READWRITE = READONLY | WRITEONLY

    def __init__(self, access_type=READWRITE, typehint=None):
        self.read = bool(access_type & XenProperty.READONLY)
        self.write = bool(access_type & XenProperty.WRITEONLY)
        self.type = typehint

    def __set_name__(self, owner, name):
        self._target = owner
        self._field = name
        if self.type is None and hasattr(owner, '__annotations__'):
            self.type = owner.__annotations__.get(self._field, inspect.Signature.empty)
        if self.read:
            methodname_get = 'get_' + self._field
            sig = inspect.Signature([inspect.Parameter('self', inspect.Parameter.POSITIONAL_OR_KEYWORD)],
                                    return_annotation=self.type)
            self.fget = XenMethod(methodname=methodname_get, sig=sig)
            self.fget.__qualname__ = owner.__qualname__ + '.' + methodname_get
            setattr(owner, methodname_get, self.fget)
        if self.write:
            methodname_set = 'set_' + self._field
            sig = inspect.Signature([inspect.Parameter('self', inspect.Parameter.POSITIONAL_OR_KEYWORD),
                                     inspect.Parameter('value', inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=self.type)])
            self.fset = XenMethod(methodname=methodname_set, sig=sig)
            self.fset.__qualname__ = owner.__qualname__ + '.' + methodname_set
            setattr(owner, methodname_set, self.fset)

    def __get__(self, instance: XenEndpoint, owner=None):
        if not self.read:
            raise AttributeError('Unreadable attribute')
        return self.fget(instance)

    def __set__(self, instance, value):
        if not self.write:
            raise AttributeError('Can\'t set attribute')
        self.fset(instance, value)
