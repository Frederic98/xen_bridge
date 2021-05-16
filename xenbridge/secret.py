#Automatically generated from https://xapi-project.github.io/xen-api/classes/secret.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class Secret(XenObject):
    xenpath='secret'

    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'other_config')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')
    value: str = XenProperty(XenProperty.READWRITE, 'the secret')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given secret."""
    @XenMethod
    def destroy(self) -> None:
        """Destroy the specified secret instance."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given secret."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given secret.  If the key is not in that Map, then do nothing."""


class SecretEndpoint(XenEndpoint):
    xenpath='secret'
    @XenMethod
    def create(self, args: Dict[str, Any]) -> 'xenbridge.Secret':
        """Create a new secret instance, and return its handle. The constructor args are:
        value*, other_config (* = non-optional)."""
    @XenMethod
    def get_all(self) -> List['xenbridge.Secret']:
        """Return a list of all the secrets known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.Secret', Dict[str, Any]]:
        """Return a map of secret references to secret records for all secrets known to the
        system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.Secret':
        """Get a reference to the secret instance with the specified UUID."""
