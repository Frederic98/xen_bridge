#Automatically generated from https://xapi-project.github.io/xen-api/classes/session.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class Session(XenObject):
    xenpath='session'

    auth_user_name: str = XenProperty(XenProperty.READONLY, 'the subject name of the user that was externally authenticated. If a session instance has is_local_superuser set, then the value of this field is undefined.')
    auth_user_sid: str = XenProperty(XenProperty.READONLY, 'the subject identifier of the user that was externally authenticated. If a session instance has is_local_superuser set, then the value of this field is undefined.')
    is_local_superuser: bool = XenProperty(XenProperty.READONLY, 'true iff this session was created using local superuser credentials')
    last_active: datetime.datetime = XenProperty(XenProperty.READONLY, 'Timestamp for last time session was active')
    originator: str = XenProperty(XenProperty.READONLY, 'a key string provided by a API user to distinguish itself from other users sharing the same login name')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    parent: 'xenbridge.Session' = XenProperty(XenProperty.READONLY, 'references the parent session that created this session')
    pool: bool = XenProperty(XenProperty.READONLY, 'True if this session relates to a intra-pool login, false otherwise')
    rbac_permissions: List[str] = XenProperty(XenProperty.READONLY, 'list with all RBAC permissions for this session')
    subject: 'xenbridge.Subject' = XenProperty(XenProperty.READONLY, 'references the subject instance that created the session. If a session instance has is_local_superuser set, then the value of this field is undefined.')
    tasks: List['xenbridge.Task'] = XenProperty(XenProperty.READONLY, 'list of tasks created using the current session')
    this_host: 'xenbridge.Host' = XenProperty(XenProperty.READONLY, 'Currently connected host')
    this_user: 'xenbridge.User' = XenProperty(XenProperty.READONLY, 'Currently connected user')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')
    validation_time: datetime.datetime = XenProperty(XenProperty.READONLY, 'time when session was last validated')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given session."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given session."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given session.  If the key is not in that Map, then do nothing."""


class SessionEndpoint(XenEndpoint):
    xenpath='session'
    @XenMethod
    def change_password(self, old_pwd: str, new_pwd: str) -> None:
        """Change the account password; if your session is authenticated with root
        priviledges then the old_pwd is validated and the new_pwd is set regardless"""
    @XenMethod
    def create_from_db_file(self, filename: str) -> 'xenbridge.Session':
        ...
    @XenMethod
    def get_all_subject_identifiers(self) -> List[str]:
        """Return a list of all the user subject-identifiers of all existing sessions"""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.Session':
        """Get a reference to the session instance with the specified UUID."""
    @XenMethod
    def local_logout(self) -> None:
        """Log out of local session."""
    @XenMethod
    def logout(self) -> None:
        """Log out of a session"""
    @XenMethod
    def logout_subject_identifier(self, subject_identifier: str) -> None:
        """Log out all sessions associated to a user subject-identifier, except the session
        associated with the context calling this function"""
