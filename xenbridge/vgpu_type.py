#Automatically generated from https://xapi-project.github.io/xen-api/classes/vgpu_type.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class VgpuTypeImplementation(XenEnum):
    PASSTHROUGH = 'passthrough'
    NVIDIA = 'nvidia'
    NVIDIA_SRIOV = 'nvidia_sriov'
    GVT_G = 'gvt_g'
    MXGPU = 'mxgpu'

class VGPUType(XenObject):
    xenpath='VGPU_type'

    VGPUs: List['xenbridge.VGPU'] = XenProperty(XenProperty.READONLY, 'List of VGPUs of this type')
    compatible_types_in_vm: List['xenbridge.VGPUType'] = XenProperty(XenProperty.READONLY, 'List of VGPU types which are compatible in one VM')
    enabled_on_GPU_groups: List['xenbridge.GPUGroup'] = XenProperty(XenProperty.READONLY, 'List of GPU groups in which at least one have this VGPU type enabled')
    enabled_on_PGPUs: List['xenbridge.PGPU'] = XenProperty(XenProperty.READONLY, 'List of PGPUs that have this VGPU type enabled')
    experimental: bool = XenProperty(XenProperty.READONLY, 'Indicates whether VGPUs of this type should be considered experimental')
    framebuffer_size: int = XenProperty(XenProperty.READONLY, 'Framebuffer size of the VGPU type, in bytes')
    identifier: str = XenProperty(XenProperty.READONLY, 'Key used to identify VGPU types and avoid creating duplicates - this field is used internally and not intended for interpretation by API clients')
    implementation: VgpuTypeImplementation = XenProperty(XenProperty.READONLY, 'The internal implementation of this VGPU type')
    max_heads: int = XenProperty(XenProperty.READONLY, 'Maximum number of displays supported by the VGPU type')
    max_resolution_x: int = XenProperty(XenProperty.READONLY, 'Maximum resolution (width) supported by the VGPU type')
    max_resolution_y: int = XenProperty(XenProperty.READONLY, 'Maximum resolution (height) supported by the VGPU type')
    model_name: str = XenProperty(XenProperty.READONLY, 'Model name associated with the VGPU type')
    supported_on_GPU_groups: List['xenbridge.GPUGroup'] = XenProperty(XenProperty.READONLY, 'List of GPU groups in which at least one PGPU supports this VGPU type')
    supported_on_PGPUs: List['xenbridge.PGPU'] = XenProperty(XenProperty.READONLY, 'List of PGPUs that support this VGPU type')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')
    vendor_name: str = XenProperty(XenProperty.READONLY, 'Name of VGPU vendor')

    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given VGPU_type."""


class VGPUTypeEndpoint(XenEndpoint):
    xenpath='VGPU_type'
    @XenMethod
    def get_all(self) -> List['xenbridge.VGPUType']:
        """Return a list of all the VGPU_types known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.VGPUType', Dict[str, Any]]:
        """Return a map of VGPU_type references to VGPU_type records for all VGPU_types
        known to the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.VGPUType':
        """Get a reference to the VGPU_type instance with the specified UUID."""
