#Automatically generated from https://xapi-project.github.io/xen-api/classes/vif_metrics.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class VIFMetrics(XenObject):
    xenpath='VIF_metrics'

    io_read_kbs: float = XenProperty(XenProperty.READONLY, 'Read bandwidth (KiB/s)')
    io_write_kbs: float = XenProperty(XenProperty.READONLY, 'Write bandwidth (KiB/s)')
    last_updated: datetime.datetime = XenProperty(XenProperty.READONLY, 'Time at which this information was last updated')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given VIF_metrics."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given VIF_metrics."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given VIF_metrics.  If the key is not in that Map, then do nothing."""


class VIFMetricsEndpoint(XenEndpoint):
    xenpath='VIF_metrics'
    @XenMethod
    def get_all(self) -> List['xenbridge.VIFMetrics']:
        """Return a list of all the VIF_metrics instances known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.VIFMetrics', Dict[str, Any]]:
        """Return a map of VIF_metrics references to VIF_metrics records for all
        VIF_metrics instances known to the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.VIFMetrics':
        """Get a reference to the VIF_metrics instance with the specified UUID."""
