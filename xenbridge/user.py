from xenbridge.xenobject import XenProperty
from .xenobject import XenEndpoint, XenObject, XenMethod


class User(XenObject):
    xenpath = 'user'

    fullname: str = XenProperty()
    short_name: str = XenProperty(XenProperty.READONLY)
    uuid: str = XenProperty(XenProperty.READONLY)

    @XenMethod
    def get_record(self): ...


class UserEndpoint(XenEndpoint):
    xenpath = 'user'

    @XenMethod
    def get_by_uuid(self, uuid: str) -> User: ...
