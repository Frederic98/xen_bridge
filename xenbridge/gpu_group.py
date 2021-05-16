#Automatically generated from https://xapi-project.github.io/xen-api/classes/gpu_group.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class AllocationAlgorithm(XenEnum):
    BREADTH_FIRST = 'breadth_first'
    DEPTH_FIRST = 'depth_first'

class GPUGroup(XenObject):
    xenpath='GPU_group'

    GPU_types: List[str] = XenProperty(XenProperty.READONLY, 'List of GPU types (vendor+device ID) that can be in this group')
    PGPUs: List['xenbridge.PGPU'] = XenProperty(XenProperty.READONLY, 'List of pGPUs in the group')
    VGPUs: List['xenbridge.VGPU'] = XenProperty(XenProperty.READONLY, 'List of vGPUs using the group')
    allocation_algorithm: AllocationAlgorithm = XenProperty(XenProperty.READWRITE, 'Current allocation of vGPUs to pGPUs for this group')
    enabled_VGPU_types: List['xenbridge.VGPUType'] = XenProperty(XenProperty.READONLY, 'vGPU types supported on at least one of the pGPUs in this group')
    name_description: str = XenProperty(XenProperty.READWRITE, 'a notes field containing human-readable description')
    name_label: str = XenProperty(XenProperty.READWRITE, 'a human-readable name')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'Additional configuration')
    supported_VGPU_types: List['xenbridge.VGPUType'] = XenProperty(XenProperty.READONLY, 'vGPU types supported on at least one of the pGPUs in this group')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given GPU_group."""
    @XenMethod
    def destroy(self) -> None:
        ...
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given GPU_group."""
    @XenMethod
    def get_remaining_capacity(self, vgpu_type: 'xenbridge.VGPUType') -> int:
        ...
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given GPU_group.  If the key is not in that Map, then do nothing."""


class GPUGroupEndpoint(XenEndpoint):
    xenpath='GPU_group'
    @XenMethod
    def create(self, name_label: str, name_description: str, other_config: Dict[str, str]) -> 'xenbridge.GPUGroup':
        ...
    @XenMethod
    def get_all(self) -> List['xenbridge.GPUGroup']:
        """Return a list of all the GPU_groups known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.GPUGroup', Dict[str, Any]]:
        """Return a map of GPU_group references to GPU_group records for all GPU_groups
        known to the system."""
    @XenMethod
    def get_by_name_label(self, label: str) -> List['xenbridge.GPUGroup']:
        """Get all the GPU_group instances with the given label."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.GPUGroup':
        """Get a reference to the GPU_group instance with the specified UUID."""
