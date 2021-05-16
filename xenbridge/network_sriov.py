#Automatically generated from https://xapi-project.github.io/xen-api/classes/network_sriov.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class SriovConfigurationMode(XenEnum):
    SYSFS = 'sysfs'
    MODPROBE = 'modprobe'
    MANUAL = 'manual'
    UNKNOWN = 'unknown'

class NetworkSriov(XenObject):
    xenpath='network_sriov'

    configuration_mode: SriovConfigurationMode = XenProperty(XenProperty.READONLY, 'The mode for configure network sriov')
    logical_PIF: 'xenbridge.PIF' = XenProperty(XenProperty.READONLY, 'The logical PIF to connect to the SR-IOV network after enable SR-IOV on the physical PIF')
    physical_PIF: 'xenbridge.PIF' = XenProperty(XenProperty.READONLY, 'The PIF that has SR-IOV enabled')
    requires_reboot: bool = XenProperty(XenProperty.READONLY, 'Indicates whether the host need to be rebooted before SR-IOV is enabled on the physical PIF')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def destroy(self) -> None:
        """Disable SR-IOV on the specific PIF. It will destroy the network-sriov and the
        logical PIF accordingly."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given network_sriov."""
    @XenMethod
    def get_remaining_capacity(self) -> int:
        """Get the number of free SR-IOV VFs on the associated PIF"""


class NetworkSriovEndpoint(XenEndpoint):
    xenpath='network_sriov'
    @XenMethod
    def create(self, pif: 'xenbridge.PIF', network: 'xenbridge.Network') -> 'xenbridge.NetworkSriov':
        """Enable SR-IOV on the specific PIF. It will create a network-sriov based on the
        specific PIF and automatically create a logical PIF to connect the specific
        network."""
    @XenMethod
    def get_all(self) -> List['xenbridge.NetworkSriov']:
        """Return a list of all the network_sriovs known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.NetworkSriov', Dict[str, Any]]:
        """Return a map of network_sriov references to network_sriov records for all
        network_sriovs known to the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.NetworkSriov':
        """Get a reference to the network_sriov instance with the specified UUID."""
