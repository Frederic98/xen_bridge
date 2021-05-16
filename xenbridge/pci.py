#Automatically generated from https://xapi-project.github.io/xen-api/classes/pci.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class PCI(XenObject):
    xenpath='PCI'

    class_name: str = XenProperty(XenProperty.READONLY, 'PCI class name')
    dependencies: List['xenbridge.PCI'] = XenProperty(XenProperty.READONLY, 'List of dependent PCI devices')
    device_name: str = XenProperty(XenProperty.READONLY, 'Device name')
    driver_name: str = XenProperty(XenProperty.READONLY, 'Driver name')
    host: 'xenbridge.Host' = XenProperty(XenProperty.READONLY, 'Physical machine that owns the PCI device')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'Additional configuration')
    pci_id: str = XenProperty(XenProperty.READONLY, 'PCI ID of the physical device')
    subsystem_device_name: str = XenProperty(XenProperty.READONLY, 'Subsystem device name')
    subsystem_vendor_name: str = XenProperty(XenProperty.READONLY, 'Subsystem vendor name')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')
    vendor_name: str = XenProperty(XenProperty.READONLY, 'Vendor name')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given PCI."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given PCI."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given PCI.  If the key is not in that Map, then do nothing."""


class PCIEndpoint(XenEndpoint):
    xenpath='PCI'
    @XenMethod
    def get_all(self) -> List['xenbridge.PCI']:
        """Return a list of all the PCIs known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.PCI', Dict[str, Any]]:
        """Return a map of PCI references to PCI records for all PCIs known to the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.PCI':
        """Get a reference to the PCI instance with the specified UUID."""
