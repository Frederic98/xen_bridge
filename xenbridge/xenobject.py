import functools
import inspect
from typing import Any
import datetime
import sys
import typing
import enum


class XenEndpoint:
    def __init__(self, connection):
        self.connection = connection
        if not hasattr(self, 'xenpath'):
            self.xenpath = self.__class__.__name__

    def call(self, methodname, *args):
        return self.connection.call(self.xenpath + '.' + methodname, *self.xen2ref(args))

    def ref2xen(self, obj, typehint):
        if typehint is None or issubclass(typehint, None.__class__):
            return None
        if typing.get_origin(typehint) is list:
            # List[x]
            hint_args = typing.get_args(typehint)
            return [self.ref2xen(itm, hint_args[0]) for itm in obj]
        if typing.get_origin(typehint) is tuple:
            # Tuple[x,y]
            hint_args = typing.get_args(typehint)
            if hint_args[-1] is Ellipsis:
                hint_args = hint_args[:-1]
                hint_args += (hint_args[-1]) * (len(obj) - len(hint_args))
            return tuple(self.ref2xen(itm, hint) for itm, hint in zip(obj, hint_args))
        if typing.get_origin(typehint) is dict:
            # Dict[x,y]
            key_hint, val_hint = typing.get_args(typehint)
            return {self.ref2xen(key, key_hint): self.ref2xen(val, val_hint) for (key, val) in obj}
        if typing.get_origin(typehint) is typing.Union:
            # Optional[x] -> Union[x, None]
            hint_arg = None
            for arg in typing.get_args(typehint):
                if not issubclass(arg, None.__class__):     # arg != NoneType
                    if hint_arg is not None:
                        raise ValueError("Type hint 'Union' not supported")
                    hint_arg = arg
            if obj is None:
                return None
            return self.ref2xen(obj, hint_arg)
        if inspect.isclass(typehint) and issubclass(typehint, (bool, int, float)):
            # Basic types
            return typehint(obj)
        if inspect.isclass(typehint) and issubclass(typehint, XenObject):
            return typehint(self.connection, obj)
        if inspect.isclass(typehint) and issubclass(typehint, XenEnum):
            return typehint(obj)
        if typehint is datetime.datetime:
            date = datetime.datetime.strptime(obj.value, '%Y%m%dT%H:%M:%SZ')
            return date.replace(tzinfo=datetime.timezone.utc)
        return obj

    @classmethod
    def xen2ref(cls, value: Any):
        if isinstance(value, (list, tuple)):
            return [cls.xen2ref(itm) for itm in value]
        if isinstance(value, dict):
            return {cls.xen2ref(key): cls.xen2ref(val) for (key, val) in value.items()}
        if isinstance(value, XenObject):
            return value.ref
        if isinstance(value, XenEnum):
            return value.value
        return value


class XenObject(XenEndpoint):
    def __init__(self, connection, ref):
        XenEndpoint.__init__(self, connection)
        self.ref = ref

    def call(self, methodname, *args):
        return XenEndpoint.call(self, methodname, self, *args)      # Add object ref (self) to arguments

    def __repr__(self):
        labels = [self.__class__.__qualname__]
        try:
            labels.append(f"'{self.name_label}'")
        except AttributeError: pass
        try:
            labels.append(f'({self.uuid})')
        except AttributeError:
            labels.append(f'at {id(self)}')
        return f"<{' '.join(labels)}>"


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
            result = self.ref2xen(result, typing.get_type_hints(getattr(self, methodname), module_ns).get('return'))
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


class XenProperty:
    READONLY = 0b01
    WRITEONLY = 0b10
    READWRITE = READONLY | WRITEONLY

    def __init__(self, access_type=READWRITE, description: str=None, typehint=None):
        self.read = bool(access_type & XenProperty.READONLY)
        self.write = bool(access_type & XenProperty.WRITEONLY)
        self.type = typehint
        if description is not None:
            self.__doc__ = description

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
                                     inspect.Parameter('value', inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=self.type)],
                                    return_annotation=None)
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


class XenEnum(enum.Enum):
    ...
