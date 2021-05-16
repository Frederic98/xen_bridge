from .auth import Auth, AuthEndpoint
from .blob import Blob, BlobEndpoint
from .bond import Bond, BondEndpoint
from .certificate import Certificate, CertificateEndpoint
from .cluster import Cluster, ClusterEndpoint
from .cluster_host import ClusterHost, ClusterHostEndpoint
from .console import Console, ConsoleEndpoint
from .crashdump import Crashdump, CrashdumpEndpoint
from .data_source import DataSource, DataSourceEndpoint
from .dr_task import DRTask, DRTaskEndpoint
from .event import Event, EventEndpoint
from .feature import Feature, FeatureEndpoint
from .gpu_group import GPUGroup, GPUGroupEndpoint
from .host import Host, HostEndpoint
from .host_cpu import HostCpu, HostCpuEndpoint
from .host_crashdump import HostCrashdump, HostCrashdumpEndpoint
from .host_metrics import HostMetrics, HostMetricsEndpoint
from .host_patch import HostPatch, HostPatchEndpoint
from .lvhd import LVHD, LVHDEndpoint
from .message import Message, MessageEndpoint
from .network import Network, NetworkEndpoint
from .network_sriov import NetworkSriov, NetworkSriovEndpoint
from .pbd import PBD, PBDEndpoint
from .pci import PCI, PCIEndpoint
from .pgpu import PGPU, PGPUEndpoint
from .pif import PIF, PIFEndpoint
from .pif_metrics import PIFMetrics, PIFMetricsEndpoint
from .pool import Pool, PoolEndpoint
from .pool_patch import PoolPatch, PoolPatchEndpoint
from .pool_update import PoolUpdate, PoolUpdateEndpoint
from .probe_result import ProbeResult, ProbeResultEndpoint
from .pusb import PUSB, PUSBEndpoint
from .pvs_cache_storage import PVSCacheStorage, PVSCacheStorageEndpoint
from .pvs_proxy import PVSProxy, PVSProxyEndpoint
from .pvs_server import PVSServer, PVSServerEndpoint
from .pvs_site import PVSSite, PVSSiteEndpoint
from .role import Role, RoleEndpoint
from .sdn_controller import SDNController, SDNControllerEndpoint
from .secret import Secret, SecretEndpoint
from .session import Session, SessionEndpoint
from .sm import SM, SMEndpoint
from .sr import SR, SREndpoint
from .sr_stat import SrStat, SrStatEndpoint
from .subject import Subject, SubjectEndpoint
from .task import Task, TaskEndpoint
from .tunnel import Tunnel, TunnelEndpoint
from .usb_group import USBGroup, USBGroupEndpoint
from .user import User, UserEndpoint
from .vbd import VBD, VBDEndpoint
from .vbd_metrics import VBDMetrics, VBDMetricsEndpoint
from .vdi import VDI, VDIEndpoint
from .vdi_nbd_server_info import VdiNbdServerInfo, VdiNbdServerInfoEndpoint
from .vgpu import VGPU, VGPUEndpoint
from .vgpu_type import VGPUType, VGPUTypeEndpoint
from .vif import VIF, VIFEndpoint
from .vif_metrics import VIFMetrics, VIFMetricsEndpoint
from .vlan import VLAN, VLANEndpoint
from .vm import VM, VMEndpoint
from .vm_appliance import VMAppliance, VMApplianceEndpoint
from .vm_guest_metrics import VMGuestMetrics, VMGuestMetricsEndpoint
from .vm_metrics import VMMetrics, VMMetricsEndpoint
from .vmpp import VMPP, VMPPEndpoint
from .vmss import VMSS, VMSSEndpoint
from .vtpm import VTPM, VTPMEndpoint
from .vusb import VUSB, VUSBEndpoint
from .xenobject import XenObject, XenEndpoint
from .xenconnection import XenConnectionBase

class XenConnection(XenConnectionBase):
    Auth: AuthEndpoint
    Blob: BlobEndpoint
    Bond: BondEndpoint
    Certificate: CertificateEndpoint
    Cluster: ClusterEndpoint
    ClusterHost: ClusterHostEndpoint
    Console: ConsoleEndpoint
    Crashdump: CrashdumpEndpoint
    DataSource: DataSourceEndpoint
    DRTask: DRTaskEndpoint
    Event: EventEndpoint
    Feature: FeatureEndpoint
    GPUGroup: GPUGroupEndpoint
    Host: HostEndpoint
    HostCpu: HostCpuEndpoint
    HostCrashdump: HostCrashdumpEndpoint
    HostMetrics: HostMetricsEndpoint
    HostPatch: HostPatchEndpoint
    LVHD: LVHDEndpoint
    Message: MessageEndpoint
    Network: NetworkEndpoint
    NetworkSriov: NetworkSriovEndpoint
    PBD: PBDEndpoint
    PCI: PCIEndpoint
    PGPU: PGPUEndpoint
    PIF: PIFEndpoint
    PIFMetrics: PIFMetricsEndpoint
    Pool: PoolEndpoint
    PoolPatch: PoolPatchEndpoint
    PoolUpdate: PoolUpdateEndpoint
    ProbeResult: ProbeResultEndpoint
    PUSB: PUSBEndpoint
    PVSCacheStorage: PVSCacheStorageEndpoint
    PVSProxy: PVSProxyEndpoint
    PVSServer: PVSServerEndpoint
    PVSSite: PVSSiteEndpoint
    Role: RoleEndpoint
    SDNController: SDNControllerEndpoint
    Secret: SecretEndpoint
    Session: SessionEndpoint
    SM: SMEndpoint
    SR: SREndpoint
    SrStat: SrStatEndpoint
    Subject: SubjectEndpoint
    Task: TaskEndpoint
    Tunnel: TunnelEndpoint
    USBGroup: USBGroupEndpoint
    User: UserEndpoint
    VBD: VBDEndpoint
    VBDMetrics: VBDMetricsEndpoint
    VDI: VDIEndpoint
    VdiNbdServerInfo: VdiNbdServerInfoEndpoint
    VGPU: VGPUEndpoint
    VGPUType: VGPUTypeEndpoint
    VIF: VIFEndpoint
    VIFMetrics: VIFMetricsEndpoint
    VLAN: VLANEndpoint
    VM: VMEndpoint
    VMAppliance: VMApplianceEndpoint
    VMGuestMetrics: VMGuestMetricsEndpoint
    VMMetrics: VMMetricsEndpoint
    VMPP: VMPPEndpoint
    VMSS: VMSSEndpoint
    VTPM: VTPMEndpoint
    VUSB: VUSBEndpoint
