import xmlrpc.client
import typing

from .vm import VM, VMEndpoint
from .session import Session
from .pci import PCI, PCIEndpoint
# from .xenobject import XenConnection


class XenConnection:
    VM: VMEndpoint

    def __init__(self, host: str, user: str, passwd: str, version='1.0'):
        self.host = host
        self.proxy = xmlrpc.client.ServerProxy(self.host)
        self.user = user
        self.passwd = passwd
        self.api_version = version
        self.session = self.login_with_password(user, passwd, version=version, originator='XenBridge')

        for member, endpoint in typing.get_type_hints(XenConnection).items():
            if not hasattr(self, member):
                setattr(self, member, endpoint(self))

    def login_with_password(self, uname, pwd, version, originator) -> Session:
        session_ref = self._call_api('session.login_with_password', uname, pwd, version, originator)
        return Session(self, session_ref)

    def call(self, method, *args):
        # Make a call with our session ID
        return self._call_api(method, *((self.session.ref,) + args))

    def _call_api(self, method: str, *args):
        # print(f'Calling {method} with {args}')
        func = self.proxy
        for attr in method.split('.'):
            func = getattr(func, attr)
        result = func(*args)
        if result['Status'] == 'Success':
            return result['Value']
        raise RuntimeError(result)
