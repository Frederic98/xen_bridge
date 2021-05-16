#Automatically generated from https://xapi-project.github.io/xen-api/classes/console.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class ConsoleProtocol(XenEnum):
    VT100 = 'vt100'
    RFB = 'rfb'
    RDP = 'rdp'

class Console(XenObject):
    xenpath='console'

    VM: 'xenbridge.VM' = XenProperty(XenProperty.READONLY, 'VM to which this console is attached')
    location: str = XenProperty(XenProperty.READONLY, 'URI for the console service')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    protocol: ConsoleProtocol = XenProperty(XenProperty.READONLY, 'the protocol used by this console')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given console."""
    @XenMethod
    def destroy(self) -> None:
        """Destroy the specified console instance."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given console."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given console.  If the key is not in that Map, then do nothing."""


class ConsoleEndpoint(XenEndpoint):
    xenpath='console'
    @XenMethod
    def create(self, args: Dict[str, Any]) -> 'xenbridge.Console':
        """Create a new console instance, and return its handle. The constructor args are:
        other_config* (* = non-optional)."""
    @XenMethod
    def get_all(self) -> List['xenbridge.Console']:
        """Return a list of all the consoles known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.Console', Dict[str, Any]]:
        """Return a map of console references to console records for all consoles known to
        the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.Console':
        """Get a reference to the console instance with the specified UUID."""
