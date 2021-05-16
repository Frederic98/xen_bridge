#Automatically generated from https://xapi-project.github.io/xen-api/classes/vusb.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class VusbOperations(XenEnum):
    ATTACH = 'attach'
    PLUG = 'plug'
    UNPLUG = 'unplug'

class VUSB(XenObject):
    xenpath='VUSB'

    USB_group: 'xenbridge.USBGroup' = XenProperty(XenProperty.READONLY, 'USB group used by the VUSB')
    VM: 'xenbridge.VM' = XenProperty(XenProperty.READONLY, 'VM that owns the VUSB')
    allowed_operations: List[VusbOperations] = XenProperty(XenProperty.READONLY, 'list of the operations allowed in this state. This list is advisory only and the server state may have changed by the time this field is read by a client.')
    current_operations: Dict[str, VusbOperations] = XenProperty(XenProperty.READONLY, 'links each of the running tasks using this object (by reference) to a current_operation enum which describes the nature of the task.')
    currently_attached: bool = XenProperty(XenProperty.READONLY, 'is the device currently attached')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'Additional configuration')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given VUSB."""
    @XenMethod
    def destroy(self) -> None:
        """Removes a VUSB record from the database"""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given VUSB."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given VUSB.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def unplug(self) -> None:
        """Unplug the vusb device from the vm."""


class VUSBEndpoint(XenEndpoint):
    xenpath='VUSB'
    @XenMethod
    def create(self, VM: 'xenbridge.VM', USB_group: 'xenbridge.USBGroup', other_config: Dict[str, str]) -> 'xenbridge.VUSB':
        """Create a new VUSB record in the database only"""
    @XenMethod
    def get_all(self) -> List['xenbridge.VUSB']:
        """Return a list of all the VUSBs known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.VUSB', Dict[str, Any]]:
        """Return a map of VUSB references to VUSB records for all VUSBs known to the
        system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.VUSB':
        """Get a reference to the VUSB instance with the specified UUID."""
