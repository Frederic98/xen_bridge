from typing import List, Any

from xenbridge.user import User
from xenbridge.xenobject import XenProperty
from .xenobject import XenEndpoint, XenObject, XenMethod


class Session(XenObject):
    xenpath = 'session'

    auth_user_name: str = XenProperty(XenProperty.READONLY)
    auth_user_sid: str = XenProperty(XenProperty.READONLY)
    is_local_superuser: str = XenProperty(XenProperty.READONLY)
    last_active = XenProperty(XenProperty.READONLY)         # ToDo: Change type
    originator: str = XenProperty(XenProperty.READONLY)
    parent: 'Session' = XenProperty(XenProperty.READONLY)
    pool: bool = XenProperty(XenProperty.READONLY)
    rbac_permissions: List[str] = XenProperty(XenProperty.READONLY)
    subject = XenProperty(XenProperty.READONLY)             # ToDo: Change type
    tasks: List[Any] = XenProperty(XenProperty.READONLY)    # ToDo: Change type
    this_host = XenProperty(XenProperty.READONLY)           # ToDo: Change type
    this_user: User = XenProperty(XenProperty.READONLY)
    uuid: str = XenProperty(XenProperty.READONLY)
    validation_time = XenProperty(XenProperty.READONLY)     # ToDo: Change type


class SessionEndpoint(XenEndpoint):
    xenpath = 'Session'

    @XenMethod
    def logout(self): ...

    @XenMethod
    def local_logout(self): ...

    @XenMethod
    def change_password(self, old_pwd: str, new_pwd: str): ...

    @XenMethod
    def create_from_db_file(self, filename: str): ...
