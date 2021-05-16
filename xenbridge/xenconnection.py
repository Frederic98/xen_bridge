import typing
from . import *
import xmlrpc.client


class XenConnectionBase:

    def __init__(self, host: str, user: str, passwd: str, version='1.0', emergency_mode=False):
        self.host = host
        self.proxy = xmlrpc.client.ServerProxy(self.host)
        self.user = user
        self.passwd = passwd
        self.api_version = version
        if emergency_mode:
            self.current_session = self.slave_local_login_with_password(user, passwd)
        else:
            self.current_session = self.login_with_password(user, passwd, version=version, originator='XenBridge')

        for member, endpoint in typing.get_type_hints(self.__class__).items():
            if not hasattr(self, member):
                setattr(self, member, endpoint(self))

    def login_with_password(self, uname, pwd, version, originator) -> Session:
        """Attempt to authenticate the user, returning a session reference if successful"""
        session_ref = self._call_api('session.login_with_password', uname, pwd, version, originator)
        return Session(self, session_ref)

    def slave_local_login_with_password(self, uname: str, pwd: str) -> Session:
        """Authenticate locally against a slave in emergency mode.
         Note the resulting sessions are only good for use on this host."""
        session_ref = self._call_api('session.slave_local_login_with_password', uname, pwd)
        return Session(self, session_ref)

    def call(self, method, *args):
        # Make a call with our session ID
        return self._call_api(method, self.current_session.ref, *args)

    def _call_api(self, method: str, *args):
        # print(f'Calling {method} with {args}')
        func = self.proxy
        for attr in method.split('.'):
            func = getattr(func, attr)
        result = func(*args)
        if result['Status'] == 'Success':
            return result['Value']
        raise RuntimeError(result)

