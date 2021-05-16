#Automatically generated from https://xapi-project.github.io/xen-api/classes/user.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class User(XenObject):
    xenpath='user'

    fullname: str = XenProperty(XenProperty.READWRITE, 'full name')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    short_name: str = XenProperty(XenProperty.READONLY, 'short name (e.g. userid)')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given user."""
    @XenMethod
    def destroy(self) -> None:
        """Destroy the specified user instance."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given user."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given user.  If the key is not in that Map, then do nothing."""


class UserEndpoint(XenEndpoint):
    xenpath='user'
    @XenMethod
    def create(self, args: Dict[str, Any]) -> 'xenbridge.User':
        """Create a new user instance, and return its handle. The constructor args are:
        short_name*, fullname*, other_config (* = non-optional)."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.User':
        """Get a reference to the user instance with the specified UUID."""
