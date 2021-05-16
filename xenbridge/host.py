#Automatically generated from https://xapi-project.github.io/xen-api/classes/host.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class HostAllowedOperations(XenEnum):
    PROVISION = 'provision'
    EVACUATE = 'evacuate'
    SHUTDOWN = 'shutdown'
    REBOOT = 'reboot'
    POWER_ON = 'power_on'
    VM_START = 'vm_start'
    VM_RESUME = 'vm_resume'
    VM_MIGRATE = 'vm_migrate'
class HostDisplay(XenEnum):
    ENABLED = 'enabled'
    DISABLE_ON_REBOOT = 'disable_on_reboot'
    DISABLED = 'disabled'
    ENABLE_ON_REBOOT = 'enable_on_reboot'

class Host(XenObject):
    xenpath='host'

    API_version_major: int = XenProperty(XenProperty.READONLY, 'major version number')
    API_version_minor: int = XenProperty(XenProperty.READONLY, 'minor version number')
    API_version_vendor: str = XenProperty(XenProperty.READONLY, 'identification of vendor')
    API_version_vendor_implementation: Dict[str, str] = XenProperty(XenProperty.READONLY, 'details of vendor implementation')
    PBDs: List['xenbridge.PBD'] = XenProperty(XenProperty.READONLY, 'physical blockdevices')
    PCIs: List['xenbridge.PCI'] = XenProperty(XenProperty.READONLY, 'List of PCI devices in the host')
    PGPUs: List['xenbridge.PGPU'] = XenProperty(XenProperty.READONLY, 'List of physical GPUs in the host')
    PIFs: List['xenbridge.PIF'] = XenProperty(XenProperty.READONLY, 'physical network interfaces')
    PUSBs: List['xenbridge.PUSB'] = XenProperty(XenProperty.READONLY, 'List of physical USBs in the host')
    address: str = XenProperty(XenProperty.READWRITE, 'The address by which this host can be contacted from any other host in the pool')
    allowed_operations: List[HostAllowedOperations] = XenProperty(XenProperty.READONLY, 'list of the operations allowed in this state. This list is advisory only and the server state may have changed by the time this field is read by a client.')
    bios_strings: Dict[str, str] = XenProperty(XenProperty.READONLY, 'BIOS strings')
    blobs: Dict[str, 'xenbridge.Blob'] = XenProperty(XenProperty.READONLY, 'Binary blobs associated with this host')
    capabilities: List[str] = XenProperty(XenProperty.READONLY, 'Xen capabilities')
    certificates: List['xenbridge.Certificate'] = XenProperty(XenProperty.READONLY, 'List of certificates installed in the host')
    chipset_info: Dict[str, str] = XenProperty(XenProperty.READONLY, 'Information about chipset features')
    control_domain: 'xenbridge.VM' = XenProperty(XenProperty.READONLY, 'The control domain (domain 0)')
    cpu_configuration: Dict[str, str] = XenProperty(XenProperty.READONLY, 'The CPU configuration on this host.  May contain keys such as "nr_nodes", "sockets_per_node", "cores_per_socket", or "threads_per_core"')
    cpu_info: Dict[str, str] = XenProperty(XenProperty.READONLY, 'Details about the physical CPUs on this host')
    crash_dump_sr: 'xenbridge.SR' = XenProperty(XenProperty.READWRITE, 'The SR in which VDIs for crash dumps are created')
    crashdumps: List['xenbridge.HostCrashdump'] = XenProperty(XenProperty.READONLY, 'Set of host crash dumps')
    current_operations: Dict[str, HostAllowedOperations] = XenProperty(XenProperty.READONLY, 'links each of the running tasks using this object (by reference) to a current_operation enum which describes the nature of the task.')
    display: HostDisplay = XenProperty(XenProperty.READWRITE, 'indicates whether the host is configured to output its console to a physical display device')
    edition: str = XenProperty(XenProperty.READONLY, 'Product edition')
    editions: List[str] = XenProperty(XenProperty.READONLY, 'List of all available product editions')
    enabled: bool = XenProperty(XenProperty.READONLY, 'True if the host is currently enabled')
    external_auth_configuration: Dict[str, str] = XenProperty(XenProperty.READONLY, 'configuration specific to external authentication service')
    external_auth_service_name: str = XenProperty(XenProperty.READONLY, 'name of external authentication service configured; empty if none configured.')
    external_auth_type: str = XenProperty(XenProperty.READONLY, 'type of external authentication service configured; empty if none configured.')
    features: List['xenbridge.Feature'] = XenProperty(XenProperty.READONLY, 'List of features available on this host')
    guest_VCPUs_params: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'VCPUs params to apply to all resident guests')
    ha_network_peers: List[str] = XenProperty(XenProperty.READONLY, 'The set of hosts visible via the network from this host')
    ha_statefiles: List[str] = XenProperty(XenProperty.READONLY, 'The set of statefiles accessible from this host')
    host_CPUs: List['xenbridge.HostCpu'] = XenProperty(XenProperty.READONLY, 'The physical CPUs on this host')
    hostname: str = XenProperty(XenProperty.READWRITE, 'The hostname of this host')
    iscsi_iqn: str = XenProperty(XenProperty.READONLY, 'The initiator IQN for the host')
    license_params: Dict[str, str] = XenProperty(XenProperty.READONLY, 'State of the current license')
    license_server: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'Contact information of the license server')
    local_cache_sr: 'xenbridge.SR' = XenProperty(XenProperty.READONLY, 'The SR that is used as a local cache')
    logging: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'logging configuration')
    memory_overhead: int = XenProperty(XenProperty.READONLY, 'Virtualization memory overhead (bytes).')
    metrics: 'xenbridge.HostMetrics' = XenProperty(XenProperty.READONLY, 'metrics associated with this host')
    multipathing: bool = XenProperty(XenProperty.READONLY, 'Specifies whether multipathing is enabled')
    name_description: str = XenProperty(XenProperty.READWRITE, 'a notes field containing human-readable description')
    name_label: str = XenProperty(XenProperty.READWRITE, 'a human-readable name')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    patches: List['xenbridge.HostPatch'] = XenProperty(XenProperty.READONLY, 'Set of host patches')
    power_on_config: Dict[str, str] = XenProperty(XenProperty.READONLY, 'The power on config')
    power_on_mode: str = XenProperty(XenProperty.READONLY, 'The power on mode')
    resident_VMs: List['xenbridge.VM'] = XenProperty(XenProperty.READONLY, 'list of VMs currently resident on host')
    sched_policy: str = XenProperty(XenProperty.READONLY, 'Scheduler policy currently in force on this host')
    software_version: Dict[str, str] = XenProperty(XenProperty.READONLY, 'version strings')
    ssl_legacy: bool = XenProperty(XenProperty.READONLY, 'Allow SSLv3 protocol and ciphersuites as used by older server versions. This controls both incoming and outgoing connections. When this is set to a different value, the host immediately restarts its SSL/TLS listening service; typically this takes less than a second but existing connections to it will be broken. API login sessions will remain valid.')
    supported_bootloaders: List[str] = XenProperty(XenProperty.READONLY, 'a list of the bootloaders installed on the machine')
    suspend_image_sr: 'xenbridge.SR' = XenProperty(XenProperty.READWRITE, 'The SR in which VDIs for suspend images are created')
    tags: List[str] = XenProperty(XenProperty.READWRITE, 'user-specified tags for categorization purposes')
    uefi_certificates: str = XenProperty(XenProperty.READONLY, 'The UEFI certificates allowing Secure Boot')
    updates: List['xenbridge.PoolUpdate'] = XenProperty(XenProperty.READONLY, 'Set of updates')
    updates_requiring_reboot: List['xenbridge.PoolUpdate'] = XenProperty(XenProperty.READONLY, 'List of updates which require reboot')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')
    virtual_hardware_platform_versions: List[int] = XenProperty(XenProperty.READONLY, 'The set of versions of the virtual hardware platform that the host can offer to its guests')

    @XenMethod
    def add_tags(self, value: str) -> None:
        """Add the given value to the tags field of the given host.  If the value is
        already in that Set, then do nothing."""
    @XenMethod
    def add_to_guest_VCPUs_params(self, key: str, value: str) -> None:
        """Add the given key-value pair to the guest_VCPUs_params field of the given host."""
    @XenMethod
    def add_to_license_server(self, key: str, value: str) -> None:
        """Add the given key-value pair to the license_server field of the given host."""
    @XenMethod
    def add_to_logging(self, key: str, value: str) -> None:
        """Add the given key-value pair to the logging field of the given host."""
    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given host."""
    @XenMethod
    def apply_edition(self, edition: str, force: bool) -> None:
        """Change to another edition, or reactivate the current edition after a license has
        expired. This may be subject to the successful checkout of an appropriate
        license."""
    @XenMethod
    def assert_can_evacuate(self) -> None:
        """Check this host can be evacuated."""
    @XenMethod
    def backup_rrds(self, delay: float) -> None:
        """This causes the RRDs to be backed up to the master"""
    @XenMethod
    def bugreport_upload(self, url: str, options: Dict[str, str]) -> None:
        """Run xen-bugtool --yestoall and upload the output to support"""
    @XenMethod
    def call_extension(self, call: str) -> str:
        """Call an API extension on this host"""
    @XenMethod
    def call_plugin(self, plugin: str, fn: str, args: Dict[str, str]) -> str:
        """Call an API plugin on this host"""
    @XenMethod
    def compute_free_memory(self) -> int:
        """Computes the amount of free memory on the host."""
    @XenMethod
    def compute_memory_overhead(self) -> int:
        """Computes the virtualization memory overhead of a host."""
    @XenMethod
    def create_new_blob(self, name: str, mime_type: str, public: bool) -> 'xenbridge.Blob':
        """Create a placeholder for a named binary blob of data that is associated with
        this host"""
    @XenMethod
    def declare_dead(self) -> None:
        """Declare that a host is dead. This is a dangerous operation, and should only be
        called if the administrator is absolutely sure the host is definitely dead"""
    @XenMethod
    def destroy(self) -> None:
        """Destroy specified host record in database"""
    @XenMethod
    def disable(self) -> None:
        """Puts the host into a state in which no new VMs can be started. Currently active
        VMs on the host continue to execute."""
    @XenMethod
    def disable_display(self) -> HostDisplay:
        """Disable console output to the physical display device next time this host boots"""
    @XenMethod
    def disable_external_auth(self, config: Dict[str, str]) -> None:
        """This call disables external authentication on the local host"""
    @XenMethod
    def disable_local_storage_caching(self) -> None:
        """Disable the use of a local SR for caching purposes"""
    @XenMethod
    def dmesg(self) -> str:
        """Get the host xen dmesg."""
    @XenMethod
    def dmesg_clear(self) -> str:
        """Get the host xen dmesg, and clear the buffer."""
    @XenMethod
    def enable(self) -> None:
        """Puts the host into a state in which new VMs can be started."""
    @XenMethod
    def enable_display(self) -> HostDisplay:
        """Enable console output to the physical display device next time this host boots"""
    @XenMethod
    def enable_external_auth(self, config: Dict[str, str], service_name: str, auth_type: str) -> None:
        """This call enables external authentication on a host"""
    @XenMethod
    def enable_local_storage_caching(self, sr: 'xenbridge.SR') -> None:
        """Enable the use of a local SR for caching purposes"""
    @XenMethod
    def evacuate(self) -> None:
        """Migrate all VMs off of this host, where possible."""
    @XenMethod
    def forget_data_source_archives(self, data_source: str) -> None:
        """Forget the recorded statistics related to the specified data source"""
    @XenMethod
    def get_data_sources(self) -> List[Dict[str, Any]]:
        ...
    @XenMethod
    def get_log(self) -> str:
        """Get the host's log file"""
    @XenMethod
    def get_management_interface(self) -> 'xenbridge.PIF':
        """Returns the management interface for the specified host"""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given host."""
    @XenMethod
    def get_server_certificate(self) -> str:
        """Get the installed server public TLS certificate."""
    @XenMethod
    def get_server_localtime(self) -> datetime.datetime:
        """This call queries the host's clock for the current time in the host's local
        timezone"""
    @XenMethod
    def get_servertime(self) -> datetime.datetime:
        """This call queries the host's clock for the current time"""
    @XenMethod
    def get_system_status_capabilities(self) -> str:
        ...
    @XenMethod
    def get_uncooperative_resident_VMs(self) -> List['xenbridge.VM']:
        """Return a set of VMs which are not co-operating with the host's memory control
        system"""
    @XenMethod
    def get_vms_which_prevent_evacuation(self) -> Dict['xenbridge.VM', List[str]]:
        """Return a set of VMs which prevent the host being evacuated, with per-VM error
        codes"""
    @XenMethod
    def has_extension(self, name: str) -> bool:
        """Return true if the extension is available on the host"""
    @XenMethod
    def install_server_certificate(self, certificate: str, private_key: str, certificate_chain: str) -> None:
        """Install the TLS server certificate."""
    @XenMethod
    def license_add(self, contents: str) -> None:
        """Apply a new license to a host"""
    @XenMethod
    def license_apply(self, contents: str) -> None:
        """Apply a new license to a host"""
    @XenMethod
    def license_remove(self) -> None:
        """Remove any license file from the specified host, and switch that host to the
        unlicensed edition"""
    @XenMethod
    def migrate_receive(self, network: 'xenbridge.Network', options: Dict[str, str]) -> Dict[str, str]:
        """Prepare to receive a VM, returning a token which can be passed to VM.migrate."""
    @XenMethod
    def power_on(self) -> None:
        """Attempt to power-on the host (if the capability exists)."""
    @XenMethod
    def query_data_source(self, data_source: str) -> float:
        """Query the latest value of the specified data source"""
    @XenMethod
    def reboot(self) -> None:
        """Reboot the host. (This function can only be called if there are no currently
        running VMs on the host and it is disabled.)"""
    @XenMethod
    def record_data_source(self, data_source: str) -> None:
        """Start recording the specified data source"""
    @XenMethod
    def refresh_pack_info(self) -> None:
        """Refresh the list of installed Supplemental Packs."""
    @XenMethod
    def remove_from_guest_VCPUs_params(self, key: str) -> None:
        """Remove the given key and its corresponding value from the guest_VCPUs_params
        field of the given host.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_from_license_server(self, key: str) -> None:
        """Remove the given key and its corresponding value from the license_server field
        of the given host.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_from_logging(self, key: str) -> None:
        """Remove the given key and its corresponding value from the logging field of the
        given host.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given host.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_tags(self, value: str) -> None:
        """Remove the given value from the tags field of the given host.  If the value is
        not in that Set, then do nothing."""
    @XenMethod
    def reset_cpu_features(self) -> None:
        """Remove the feature mask, such that after a reboot all features of the CPU are
        enabled."""
    @XenMethod
    def restart_agent(self) -> None:
        """Restarts the agent after a 10 second pause. WARNING: this is a dangerous
        operation. Any operations in progress will be aborted, and unrecoverable data
        loss may occur. The caller is responsible for ensuring that there are no
        operations in progress when this method is called."""
    @XenMethod
    def retrieve_wlb_evacuate_recommendations(self) -> Dict['xenbridge.VM', List[str]]:
        """Retrieves recommended host migrations to perform when evacuating the host from
        the wlb server. If a VM cannot be migrated from the host the reason is listed
        instead of a recommendation."""
    @XenMethod
    def send_debug_keys(self, keys: str) -> None:
        """Inject the given string as debugging keys into Xen"""
    @XenMethod
    def set_cpu_features(self, features: str) -> None:
        """Set the CPU features to be used after a reboot, if the given features string is
        valid."""
    @XenMethod
    def set_hostname_live(self, hostname: str) -> None:
        """Sets the host name to the specified string.  Both the API and lower-level system
        hostname are changed immediately."""
    @XenMethod
    def shutdown(self) -> None:
        """Shutdown the host. (This function can only be called if there are no currently
        running VMs on the host and it is disabled.)"""
    @XenMethod
    def sync_data(self) -> None:
        """This causes the synchronisation of the non-database data (messages, RRDs and so
        on) stored on the master to be synchronised with the host"""
    @XenMethod
    def syslog_reconfigure(self) -> None:
        """Re-configure syslog logging"""


class HostEndpoint(XenEndpoint):
    xenpath='host'
    @XenMethod
    def emergency_ha_disable(self, soft: bool) -> None:
        """This call disables HA on the local host. This should only be used with extreme
        care."""
    @XenMethod
    def emergency_reset_server_certificate(self) -> None:
        """Delete the current TLS server certificate and replace by a new, self-signed one.
        This should only be used with extreme care."""
    @XenMethod
    def get_all(self) -> List['xenbridge.Host']:
        """Return a list of all the hosts known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.Host', Dict[str, Any]]:
        """Return a map of host references to host records for all hosts known to the
        system."""
    @XenMethod
    def get_by_name_label(self, label: str) -> List['xenbridge.Host']:
        """Get all the host instances with the given label."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.Host':
        """Get a reference to the host instance with the specified UUID."""
    @XenMethod
    def list_methods(self) -> List[str]:
        """List all supported methods"""
    @XenMethod
    def local_management_reconfigure(self, interface: str) -> None:
        """Reconfigure the management network interface. Should only be used if
        Host.management_reconfigure is impossible because the network configuration is
        broken."""
    @XenMethod
    def management_disable(self) -> None:
        """Disable the management network interface"""
    @XenMethod
    def management_reconfigure(self, pif: 'xenbridge.PIF') -> None:
        """Reconfigure the management network interface"""
    @XenMethod
    def shutdown_agent(self) -> None:
        """Shuts the agent down after a 10 second pause. WARNING: this is a dangerous
        operation. Any operations in progress will be aborted, and unrecoverable data
        loss may occur. The caller is responsible for ensuring that there are no
        operations in progress when this method is called."""
