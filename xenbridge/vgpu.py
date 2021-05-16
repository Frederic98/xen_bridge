#Automatically generated from https://xapi-project.github.io/xen-api/classes/vgpu.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class VGPU(XenObject):
    xenpath='VGPU'

    GPU_group: 'xenbridge.GPUGroup' = XenProperty(XenProperty.READONLY, 'GPU group used by the vGPU')
    PCI: 'xenbridge.PCI' = XenProperty(XenProperty.READONLY, 'Device passed trough to VM, either as full device or SR-IOV virtual function')
    VM: 'xenbridge.VM' = XenProperty(XenProperty.READONLY, 'VM that owns the vGPU')
    compatibility_metadata: Dict[str, str] = XenProperty(XenProperty.READONLY, 'VGPU metadata to determine whether a VGPU can migrate between two PGPUs')
    currently_attached: bool = XenProperty(XenProperty.READONLY, 'Reflects whether the virtual device is currently connected to a physical device')
    device: str = XenProperty(XenProperty.READONLY, 'Order in which the devices are plugged into the VM')
    extra_args: str = XenProperty(XenProperty.READWRITE, 'Extra arguments for vGPU and passed to demu')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'Additional configuration')
    resident_on: 'xenbridge.PGPU' = XenProperty(XenProperty.READONLY, 'The PGPU on which this VGPU is running')
    scheduled_to_be_resident_on: 'xenbridge.PGPU' = XenProperty(XenProperty.READONLY, 'The PGPU on which this VGPU is scheduled to run')
    type: 'xenbridge.VGPUType' = XenProperty(XenProperty.READONLY, 'Preset type for this VGPU')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given VGPU."""
    @XenMethod
    def destroy(self) -> None:
        ...
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given VGPU."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given VGPU.  If the key is not in that Map, then do nothing."""


class VGPUEndpoint(XenEndpoint):
    xenpath='VGPU'
    @XenMethod
    def create(self, VM: 'xenbridge.VM', GPU_group: 'xenbridge.GPUGroup', device: str, other_config: Dict[str, str], type: 'xenbridge.VGPUType') -> 'xenbridge.VGPU':
        ...
    @XenMethod
    def get_all(self) -> List['xenbridge.VGPU']:
        """Return a list of all the VGPUs known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.VGPU', Dict[str, Any]]:
        """Return a map of VGPU references to VGPU records for all VGPUs known to the
        system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.VGPU':
        """Get a reference to the VGPU instance with the specified UUID."""
