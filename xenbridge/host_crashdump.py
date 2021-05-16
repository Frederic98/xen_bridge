#Automatically generated from https://xapi-project.github.io/xen-api/classes/host_crashdump.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class HostCrashdump(XenObject):
    xenpath='host_crashdump'

    host: 'xenbridge.Host' = XenProperty(XenProperty.READONLY, 'Host the crashdump relates to')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    size: int = XenProperty(XenProperty.READONLY, 'Size of the crashdump')
    timestamp: datetime.datetime = XenProperty(XenProperty.READONLY, 'Time the crash happened')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given
        host_crashdump."""
    @XenMethod
    def destroy(self) -> None:
        """Destroy specified host crash dump, removing it from the disk."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given host_crashdump."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given host_crashdump.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def upload(self, url: str, options: Dict[str, str]) -> None:
        """Upload the specified host crash dump to a specified URL"""


class HostCrashdumpEndpoint(XenEndpoint):
    xenpath='host_crashdump'
    @XenMethod
    def get_all(self) -> List['xenbridge.HostCrashdump']:
        """Return a list of all the host_crashdumps known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.HostCrashdump', Dict[str, Any]]:
        """Return a map of host_crashdump references to host_crashdump records for all
        host_crashdumps known to the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.HostCrashdump':
        """Get a reference to the host_crashdump instance with the specified UUID."""
