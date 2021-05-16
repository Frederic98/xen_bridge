#Automatically generated from https://xapi-project.github.io/xen-api/classes/crashdump.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class Crashdump(XenObject):
    xenpath='crashdump'

    VDI: 'xenbridge.VDI' = XenProperty(XenProperty.READONLY, 'the virtual disk')
    VM: 'xenbridge.VM' = XenProperty(XenProperty.READONLY, 'the virtual machine')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given crashdump."""
    @XenMethod
    def destroy(self) -> None:
        """Destroy the specified crashdump"""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given crashdump."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given crashdump.  If the key is not in that Map, then do nothing."""


class CrashdumpEndpoint(XenEndpoint):
    xenpath='crashdump'
    @XenMethod
    def get_all(self) -> List['xenbridge.Crashdump']:
        """Return a list of all the crashdumps known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.Crashdump', Dict[str, Any]]:
        """Return a map of crashdump references to crashdump records for all crashdumps
        known to the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.Crashdump':
        """Get a reference to the crashdump instance with the specified UUID."""
