#Automatically generated from https://xapi-project.github.io/xen-api/classes/host_metrics.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class HostMetrics(XenObject):
    xenpath='host_metrics'

    last_updated: datetime.datetime = XenProperty(XenProperty.READONLY, 'Time at which this information was last updated')
    live: bool = XenProperty(XenProperty.READONLY, 'Pool master thinks this host is live')
    memory_free: int = XenProperty(XenProperty.READONLY, 'Free host memory (bytes)')
    memory_total: int = XenProperty(XenProperty.READONLY, 'Total host memory (bytes)')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given
        host_metrics."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given host_metrics."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given host_metrics.  If the key is not in that Map, then do nothing."""


class HostMetricsEndpoint(XenEndpoint):
    xenpath='host_metrics'
    @XenMethod
    def get_all(self) -> List['xenbridge.HostMetrics']:
        """Return a list of all the host_metrics instances known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.HostMetrics', Dict[str, Any]]:
        """Return a map of host_metrics references to host_metrics records for all
        host_metrics instances known to the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.HostMetrics':
        """Get a reference to the host_metrics instance with the specified UUID."""
