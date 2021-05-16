#Automatically generated from https://xapi-project.github.io/xen-api/classes/host_cpu.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class HostCpu(XenObject):
    xenpath='host_cpu'

    family: int = XenProperty(XenProperty.READONLY, 'the family (number) of the physical CPU')
    features: str = XenProperty(XenProperty.READONLY, 'the physical CPU feature bitmap')
    flags: str = XenProperty(XenProperty.READONLY, 'the flags of the physical CPU (a decoded version of the features field)')
    host: 'xenbridge.Host' = XenProperty(XenProperty.READONLY, 'the host the CPU is in')
    model: int = XenProperty(XenProperty.READONLY, 'the model number of the physical CPU')
    modelname: str = XenProperty(XenProperty.READONLY, 'the model name of the physical CPU')
    number: int = XenProperty(XenProperty.READONLY, 'the number of the physical CPU within the host')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    speed: int = XenProperty(XenProperty.READONLY, 'the speed of the physical CPU')
    stepping: str = XenProperty(XenProperty.READONLY, 'the stepping of the physical CPU')
    utilisation: float = XenProperty(XenProperty.READONLY, 'the current CPU utilisation')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')
    vendor: str = XenProperty(XenProperty.READONLY, 'the vendor of the physical CPU')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given host_cpu."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given host_cpu."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given host_cpu.  If the key is not in that Map, then do nothing."""


class HostCpuEndpoint(XenEndpoint):
    xenpath='host_cpu'
    @XenMethod
    def get_all(self) -> List['xenbridge.HostCpu']:
        """Return a list of all the host_cpus known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.HostCpu', Dict[str, Any]]:
        """Return a map of host_cpu references to host_cpu records for all host_cpus known
        to the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.HostCpu':
        """Get a reference to the host_cpu instance with the specified UUID."""
