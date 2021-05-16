#Automatically generated from https://xapi-project.github.io/xen-api/classes/vm_metrics.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class DomainType(XenEnum):
    HVM = 'hvm'
    PV = 'pv'
    PV_IN_PVH = 'pv_in_pvh'
    UNSPECIFIED = 'unspecified'

class VMMetrics(XenObject):
    xenpath='VM_metrics'

    VCPUs_CPU: Dict[int, int] = XenProperty(XenProperty.READONLY, 'VCPU to PCPU map')
    VCPUs_flags: Dict[int, List[str]] = XenProperty(XenProperty.READONLY, 'CPU flags (blocked,online,running)')
    VCPUs_number: int = XenProperty(XenProperty.READONLY, 'Current number of VCPUs')
    VCPUs_params: Dict[str, str] = XenProperty(XenProperty.READONLY, 'The live equivalent to VM.VCPUs_params')
    VCPUs_utilisation: Dict[int, float] = XenProperty(XenProperty.READONLY, "Utilisation for all of guest's current VCPUs")
    current_domain_type: DomainType = XenProperty(XenProperty.READONLY, 'The current domain type of the VM (for running,suspended, or paused VMs). The last-known domain type for halted VMs.')
    hvm: bool = XenProperty(XenProperty.READONLY, 'hardware virtual machine')
    install_time: datetime.datetime = XenProperty(XenProperty.READONLY, 'Time at which the VM was installed')
    last_updated: datetime.datetime = XenProperty(XenProperty.READONLY, 'Time at which this information was last updated')
    memory_actual: int = XenProperty(XenProperty.READONLY, "Guest's actual memory (bytes)")
    nested_virt: bool = XenProperty(XenProperty.READONLY, 'VM supports nested virtualisation')
    nomigrate: bool = XenProperty(XenProperty.READONLY, "VM is immobile and can't migrate between hosts")
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    start_time: datetime.datetime = XenProperty(XenProperty.READONLY, 'Time at which this VM was last booted')
    state: List[str] = XenProperty(XenProperty.READONLY, 'The state of the guest, eg blocked, dying etc')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given VM_metrics."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given VM_metrics."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given VM_metrics.  If the key is not in that Map, then do nothing."""


class VMMetricsEndpoint(XenEndpoint):
    xenpath='VM_metrics'
    @XenMethod
    def get_all(self) -> List['xenbridge.VMMetrics']:
        """Return a list of all the VM_metrics instances known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.VMMetrics', Dict[str, Any]]:
        """Return a map of VM_metrics references to VM_metrics records for all VM_metrics
        instances known to the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.VMMetrics':
        """Get a reference to the VM_metrics instance with the specified UUID."""
