#Automatically generated from https://xapi-project.github.io/xen-api/classes/usb_group.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class USBGroup(XenObject):
    xenpath='USB_group'

    PUSBs: List['xenbridge.PUSB'] = XenProperty(XenProperty.READONLY, 'List of PUSBs in the group')
    VUSBs: List['xenbridge.VUSB'] = XenProperty(XenProperty.READONLY, 'List of VUSBs using the group')
    name_description: str = XenProperty(XenProperty.READWRITE, 'a notes field containing human-readable description')
    name_label: str = XenProperty(XenProperty.READWRITE, 'a human-readable name')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'Additional configuration')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given USB_group."""
    @XenMethod
    def destroy(self) -> None:
        ...
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given USB_group."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given USB_group.  If the key is not in that Map, then do nothing."""


class USBGroupEndpoint(XenEndpoint):
    xenpath='USB_group'
    @XenMethod
    def create(self, name_label: str, name_description: str, other_config: Dict[str, str]) -> 'xenbridge.USBGroup':
        ...
    @XenMethod
    def get_all(self) -> List['xenbridge.USBGroup']:
        """Return a list of all the USB_groups known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.USBGroup', Dict[str, Any]]:
        """Return a map of USB_group references to USB_group records for all USB_groups
        known to the system."""
    @XenMethod
    def get_by_name_label(self, label: str) -> List['xenbridge.USBGroup']:
        """Get all the USB_group instances with the given label."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.USBGroup':
        """Get a reference to the USB_group instance with the specified UUID."""
