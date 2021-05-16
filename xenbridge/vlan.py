#Automatically generated from https://xapi-project.github.io/xen-api/classes/vlan.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class VLAN(XenObject):
    xenpath='VLAN'

    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    tag: int = XenProperty(XenProperty.READONLY, 'VLAN tag in use')
    tagged_PIF: 'xenbridge.PIF' = XenProperty(XenProperty.READONLY, 'interface on which traffic is tagged')
    untagged_PIF: 'xenbridge.PIF' = XenProperty(XenProperty.READONLY, 'interface on which traffic is untagged')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given VLAN."""
    @XenMethod
    def destroy(self) -> None:
        """Destroy a VLAN mux/demuxer"""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given VLAN."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given VLAN.  If the key is not in that Map, then do nothing."""


class VLANEndpoint(XenEndpoint):
    xenpath='VLAN'
    @XenMethod
    def create(self, tagged_PIF: 'xenbridge.PIF', tag: int, network: 'xenbridge.Network') -> 'xenbridge.VLAN':
        """Create a VLAN mux/demuxer"""
    @XenMethod
    def get_all(self) -> List['xenbridge.VLAN']:
        """Return a list of all the VLANs known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.VLAN', Dict[str, Any]]:
        """Return a map of VLAN references to VLAN records for all VLANs known to the
        system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.VLAN':
        """Get a reference to the VLAN instance with the specified UUID."""
