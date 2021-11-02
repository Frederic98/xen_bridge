import typing
from . import Session, XenError
import xmlrpc.client
try:
    import requests
except ImportError:
    requests = None


class XenConnectionBase:

    def __init__(self, host: str, user: str, passwd: str, version='1.0', emergency_mode=False, **kwargs):
        self.host = host
        self.proxy = xmlrpc.client.ServerProxy(self.host, **kwargs)
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
        elif result['Status'] == 'Failure':
            raise XenError(result)
        else:
            raise ValueError('Got an unknown response!')


class RequestsTransport(xmlrpc.client.Transport):
    """
    Drop in Transport for xmlrpclib that uses Requests instead of httplib
    """

    # change our user agent to reflect Requests
    user_agent = "Python XMLRPC with Requests (python-requests.org)"

    # override this if you'd like to https
    use_https = False

    def __init__(self, use_datetime=False, use_builtin_types=False,
                 *, headers=(), https=use_https, verbose=False):
        if requests is None:
            raise RuntimeError('Requests not available')
        xmlrpc.client.Transport.__init__(self,
                                         use_datetime=use_datetime,
                                         use_builtin_types=use_builtin_types,
                                         headers=headers)
        self.use_https = https
        self.verbose = verbose

    def request(self, host, handler, request_body, verbose=False):
        """
        Make an xmlrpc request.
        """
        headers = {'User-Agent': self.user_agent}
        url = self._build_url(host, handler)
        resp = requests.post(url, data=request_body, headers=headers, stream=True)
        try:
            resp.raise_for_status()
        except requests.RequestException as e:
            raise xmlrpc.client.ProtocolError(url, resp.status_code, str(e), resp.headers)
        else:
            return self.parse_response(resp.raw)

    def _build_url(self, host, handler):
        """
        Build a url for our request based on the host, handler and use_http
        property
        """
        scheme = 'https' if self.use_https else 'http'
        return '%s://%s/%s' % (scheme, host, handler)
