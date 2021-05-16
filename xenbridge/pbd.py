#Automatically generated from https://xapi-project.github.io/xen-api/classes/pbd.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class PBD(XenObject):
    xenpath='PBD'

    SR: 'xenbridge.SR' = XenProperty(XenProperty.READONLY, 'the storage repository that the pbd realises')
    currently_attached: bool = XenProperty(XenProperty.READONLY, 'When the currently_attached field is true, it means that the host has\nsuccessfully authenticated and mounted the remote storage device. In\nthe case of NFS this would typically mean the filesystem has been mounted;\nin the case of iSCSI this would typically mean that a connection to the\ntarget has been established.\nIf the connection to the storage fails (for example: if the network goes\ndown or a storage target fails), the host will keep trying to re-establish\nthe connection and the currently_attached field will remain true.\nThis implies that the currently_attached=true does not mean that the\nstorage is working well, or at all, simply that the host is trying to make\nit work.')
    device_config: Dict[str, str] = XenProperty(XenProperty.READONLY, "a config string to string map that is provided to the host's SR-backend-driver")
    host: 'xenbridge.Host' = XenProperty(XenProperty.READONLY, 'physical machine on which the pbd is available')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given PBD."""
    @XenMethod
    def destroy(self) -> None:
        """Destroy the specified PBD instance."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given PBD."""
    @XenMethod
    def plug(self) -> None:
        """Activate the specified PBD, causing the referenced SR to be attached and scanned"""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given PBD.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def unplug(self) -> None:
        """Deactivate the specified PBD, causing the referenced SR to be detached and
        nolonger scanned"""


class PBDEndpoint(XenEndpoint):
    xenpath='PBD'
    @XenMethod
    def create(self, args: Dict[str, Any]) -> 'xenbridge.PBD':
        """Create a new PBD instance, and return its handle. The constructor args are:
        host*, SR*, device_config*, other_config (* = non-optional)."""
    @XenMethod
    def get_all(self) -> List['xenbridge.PBD']:
        """Return a list of all the PBDs known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.PBD', Dict[str, Any]]:
        """Return a map of PBD references to PBD records for all PBDs known to the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.PBD':
        """Get a reference to the PBD instance with the specified UUID."""
