#Automatically generated from https://xapi-project.github.io/xen-api/classes/pgpu.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class PgpuDom0Access(XenEnum):
    ENABLED = 'enabled'
    DISABLE_ON_REBOOT = 'disable_on_reboot'
    DISABLED = 'disabled'
    ENABLE_ON_REBOOT = 'enable_on_reboot'

class PGPU(XenObject):
    xenpath='PGPU'

    GPU_group: 'xenbridge.GPUGroup' = XenProperty(XenProperty.READONLY, 'GPU group the pGPU is contained in')
    PCI: 'xenbridge.PCI' = XenProperty(XenProperty.READONLY, 'Link to underlying PCI device')
    compatibility_metadata: Dict[str, str] = XenProperty(XenProperty.READONLY, 'PGPU metadata to determine whether a VGPU can migrate between two PGPUs')
    dom0_access: PgpuDom0Access = XenProperty(XenProperty.READONLY, 'The accessibility of this device from dom0')
    enabled_VGPU_types: List['xenbridge.VGPUType'] = XenProperty(XenProperty.READONLY, 'List of VGPU types which have been enabled for this PGPU')
    host: 'xenbridge.Host' = XenProperty(XenProperty.READONLY, 'Host that owns the GPU')
    is_system_display_device: bool = XenProperty(XenProperty.READONLY, 'Is this device the system display device')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'Additional configuration')
    resident_VGPUs: List['xenbridge.VGPU'] = XenProperty(XenProperty.READONLY, 'List of VGPUs running on this PGPU')
    supported_VGPU_max_capacities: Dict['xenbridge.VGPUType', int] = XenProperty(XenProperty.READONLY, 'A map relating each VGPU type supported on this GPU to the maximum number of VGPUs of that type which can run simultaneously on this GPU')
    supported_VGPU_types: List['xenbridge.VGPUType'] = XenProperty(XenProperty.READONLY, 'List of VGPU types supported by the underlying hardware')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_enabled_VGPU_types(self, value: 'xenbridge.VGPUType') -> None:
        ...
    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given PGPU."""
    @XenMethod
    def disable_dom0_access(self) -> PgpuDom0Access:
        ...
    @XenMethod
    def enable_dom0_access(self) -> PgpuDom0Access:
        ...
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given PGPU."""
    @XenMethod
    def get_remaining_capacity(self, vgpu_type: 'xenbridge.VGPUType') -> int:
        ...
    @XenMethod
    def remove_enabled_VGPU_types(self, value: 'xenbridge.VGPUType') -> None:
        ...
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given PGPU.  If the key is not in that Map, then do nothing."""


class PGPUEndpoint(XenEndpoint):
    xenpath='PGPU'
    @XenMethod
    def get_all(self) -> List['xenbridge.PGPU']:
        """Return a list of all the PGPUs known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.PGPU', Dict[str, Any]]:
        """Return a map of PGPU references to PGPU records for all PGPUs known to the
        system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.PGPU':
        """Get a reference to the PGPU instance with the specified UUID."""
