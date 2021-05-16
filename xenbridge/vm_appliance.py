#Automatically generated from https://xapi-project.github.io/xen-api/classes/vm_appliance.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class VmApplianceOperation(XenEnum):
    START = 'start'
    CLEAN_SHUTDOWN = 'clean_shutdown'
    HARD_SHUTDOWN = 'hard_shutdown'
    SHUTDOWN = 'shutdown'

class VMAppliance(XenObject):
    xenpath='VM_appliance'

    VMs: List['xenbridge.VM'] = XenProperty(XenProperty.READONLY, 'all VMs in this appliance')
    allowed_operations: List[VmApplianceOperation] = XenProperty(XenProperty.READONLY, 'list of the operations allowed in this state. This list is advisory only and the server state may have changed by the time this field is read by a client.')
    current_operations: Dict[str, VmApplianceOperation] = XenProperty(XenProperty.READONLY, 'links each of the running tasks using this object (by reference) to a current_operation enum which describes the nature of the task.')
    name_description: str = XenProperty(XenProperty.READWRITE, 'a notes field containing human-readable description')
    name_label: str = XenProperty(XenProperty.READWRITE, 'a human-readable name')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def assert_can_be_recovered(self, session_to: 'xenbridge.Session') -> None:
        """Assert whether all SRs required to recover this VM appliance are available."""
    @XenMethod
    def clean_shutdown(self) -> None:
        """Perform a clean shutdown of all the VMs in the appliance"""
    @XenMethod
    def destroy(self) -> None:
        """Destroy the specified VM_appliance instance."""
    @XenMethod
    def get_SRs_required_for_recovery(self, session_to: 'xenbridge.Session') -> List['xenbridge.SR']:
        """Get the list of SRs required by the VM appliance to recover."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given VM_appliance."""
    @XenMethod
    def hard_shutdown(self) -> None:
        """Perform a hard shutdown of all the VMs in the appliance"""
    @XenMethod
    def recover(self, session_to: 'xenbridge.Session', force: bool) -> None:
        """Recover the VM appliance"""
    @XenMethod
    def shutdown(self) -> None:
        """For each VM in the appliance, try to shut it down cleanly. If this fails,
        perform a hard shutdown of the VM."""
    @XenMethod
    def start(self, paused: bool) -> None:
        """Start all VMs in the appliance"""


class VMApplianceEndpoint(XenEndpoint):
    xenpath='VM_appliance'
    @XenMethod
    def create(self, args: Dict[str, Any]) -> 'xenbridge.VMAppliance':
        """Create a new VM_appliance instance, and return its handle. The constructor args
        are: name_label, name_description (* = non-optional)."""
    @XenMethod
    def get_all(self) -> List['xenbridge.VMAppliance']:
        """Return a list of all the VM_appliances known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.VMAppliance', Dict[str, Any]]:
        """Return a map of VM_appliance references to VM_appliance records for all
        VM_appliances known to the system."""
    @XenMethod
    def get_by_name_label(self, label: str) -> List['xenbridge.VMAppliance']:
        """Get all the VM_appliance instances with the given label."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.VMAppliance':
        """Get a reference to the VM_appliance instance with the specified UUID."""
