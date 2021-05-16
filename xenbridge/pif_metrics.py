#Automatically generated from https://xapi-project.github.io/xen-api/classes/pif_metrics.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class PIFMetrics(XenObject):
    xenpath='PIF_metrics'

    carrier: bool = XenProperty(XenProperty.READONLY, 'Report if the PIF got a carrier or not')
    device_id: str = XenProperty(XenProperty.READONLY, 'Report device ID')
    device_name: str = XenProperty(XenProperty.READONLY, 'Report device name')
    duplex: bool = XenProperty(XenProperty.READONLY, 'Full duplex capability of the link (if available)')
    io_read_kbs: float = XenProperty(XenProperty.READONLY, 'Read bandwidth (KiB/s)')
    io_write_kbs: float = XenProperty(XenProperty.READONLY, 'Write bandwidth (KiB/s)')
    last_updated: datetime.datetime = XenProperty(XenProperty.READONLY, 'Time at which this information was last updated')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    pci_bus_path: str = XenProperty(XenProperty.READONLY, 'PCI bus path of the pif (if available)')
    speed: int = XenProperty(XenProperty.READONLY, 'Speed of the link (if available)')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')
    vendor_id: str = XenProperty(XenProperty.READONLY, 'Report vendor ID')
    vendor_name: str = XenProperty(XenProperty.READONLY, 'Report vendor name')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given PIF_metrics."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given PIF_metrics."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given PIF_metrics.  If the key is not in that Map, then do nothing."""


class PIFMetricsEndpoint(XenEndpoint):
    xenpath='PIF_metrics'
    @XenMethod
    def get_all(self) -> List['xenbridge.PIFMetrics']:
        """Return a list of all the PIF_metrics instances known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.PIFMetrics', Dict[str, Any]]:
        """Return a map of PIF_metrics references to PIF_metrics records for all
        PIF_metrics instances known to the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.PIFMetrics':
        """Get a reference to the PIF_metrics instance with the specified UUID."""
