#Automatically generated from https://xapi-project.github.io/xen-api/classes/pusb.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class PUSB(XenObject):
    xenpath='PUSB'

    USB_group: 'xenbridge.USBGroup' = XenProperty(XenProperty.READONLY, 'USB group the PUSB is contained in')
    description: str = XenProperty(XenProperty.READONLY, 'USB device description')
    host: 'xenbridge.Host' = XenProperty(XenProperty.READONLY, 'Physical machine that owns the USB device')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    passthrough_enabled: bool = XenProperty(XenProperty.READONLY, 'enabled for passthrough')
    path: str = XenProperty(XenProperty.READONLY, 'port path of USB device')
    product_desc: str = XenProperty(XenProperty.READONLY, 'product description of the USB device')
    product_id: str = XenProperty(XenProperty.READONLY, 'product id of the USB device')
    serial: str = XenProperty(XenProperty.READONLY, 'serial of the USB device')
    speed: float = XenProperty(XenProperty.READONLY, 'USB device speed')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')
    vendor_desc: str = XenProperty(XenProperty.READONLY, 'vendor description of the USB device')
    vendor_id: str = XenProperty(XenProperty.READONLY, 'vendor id of the USB device')
    version: str = XenProperty(XenProperty.READONLY, 'USB device version')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given PUSB."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given PUSB."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given PUSB.  If the key is not in that Map, then do nothing."""


class PUSBEndpoint(XenEndpoint):
    xenpath='PUSB'
    @XenMethod
    def get_all(self) -> List['xenbridge.PUSB']:
        """Return a list of all the PUSBs known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.PUSB', Dict[str, Any]]:
        """Return a map of PUSB references to PUSB records for all PUSBs known to the
        system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.PUSB':
        """Get a reference to the PUSB instance with the specified UUID."""
    @XenMethod
    def scan(self, host: 'xenbridge.Host') -> None:
        ...
