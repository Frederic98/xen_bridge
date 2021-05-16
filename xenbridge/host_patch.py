#Automatically generated from https://xapi-project.github.io/xen-api/classes/host_patch.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class HostPatch(XenObject):
    xenpath='host_patch'

    applied: bool = XenProperty(XenProperty.READONLY, 'True if the patch has been applied')
    host: 'xenbridge.Host' = XenProperty(XenProperty.READONLY, 'Host the patch relates to')
    name_description: str = XenProperty(XenProperty.READONLY, 'a notes field containing human-readable description')
    name_label: str = XenProperty(XenProperty.READONLY, 'a human-readable name')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    pool_patch: 'xenbridge.PoolPatch' = XenProperty(XenProperty.READONLY, 'The patch applied')
    size: int = XenProperty(XenProperty.READONLY, 'Size of the patch')
    timestamp_applied: datetime.datetime = XenProperty(XenProperty.READONLY, 'Time the patch was applied')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')
    version: str = XenProperty(XenProperty.READONLY, 'Patch version number')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given host_patch."""
    @XenMethod
    def apply(self) -> str:
        """Apply the selected patch and return its output"""
    @XenMethod
    def destroy(self) -> None:
        """Destroy the specified host patch, removing it from the disk. This does NOT
        reverse the patch"""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given host_patch."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given host_patch.  If the key is not in that Map, then do nothing."""


class HostPatchEndpoint(XenEndpoint):
    xenpath='host_patch'
    @XenMethod
    def get_all(self) -> List['xenbridge.HostPatch']:
        """Return a list of all the host_patchs known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.HostPatch', Dict[str, Any]]:
        """Return a map of host_patch references to host_patch records for all host_patchs
        known to the system."""
    @XenMethod
    def get_by_name_label(self, label: str) -> List['xenbridge.HostPatch']:
        """Get all the host_patch instances with the given label."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.HostPatch':
        """Get a reference to the host_patch instance with the specified UUID."""
