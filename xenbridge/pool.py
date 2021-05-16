#Automatically generated from https://xapi-project.github.io/xen-api/classes/pool.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class PoolAllowedOperations(XenEnum):
    HA_ENABLE = 'ha_enable'
    HA_DISABLE = 'ha_disable'
    CLUSTER_CREATE = 'cluster_create'

class Pool(XenObject):
    xenpath='pool'

    allowed_operations: List[PoolAllowedOperations] = XenProperty(XenProperty.READONLY, 'list of the operations allowed in this state. This list is advisory only and the server state may have changed by the time this field is read by a client.')
    blobs: Dict[str, 'xenbridge.Blob'] = XenProperty(XenProperty.READONLY, 'Binary blobs associated with this pool')
    cpu_info: Dict[str, str] = XenProperty(XenProperty.READONLY, 'Details about the physical CPUs on the pool')
    crash_dump_SR: 'xenbridge.SR' = XenProperty(XenProperty.READWRITE, 'The SR in which VDIs for crash dumps are created')
    current_operations: Dict[str, PoolAllowedOperations] = XenProperty(XenProperty.READONLY, 'links each of the running tasks using this object (by reference) to a current_operation enum which describes the nature of the task.')
    default_SR: 'xenbridge.SR' = XenProperty(XenProperty.READWRITE, 'Default SR for VDIs')
    guest_agent_config: Dict[str, str] = XenProperty(XenProperty.READONLY, 'Pool-wide guest agent configuration information')
    gui_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'gui-specific configuration for pool')
    ha_allow_overcommit: bool = XenProperty(XenProperty.READWRITE, 'If set to false then operations which would cause the Pool to become overcommitted will be blocked.')
    ha_cluster_stack: str = XenProperty(XenProperty.READONLY, 'The HA cluster stack that is currently in use. Only valid when HA is enabled.')
    ha_configuration: Dict[str, str] = XenProperty(XenProperty.READONLY, 'The current HA configuration')
    ha_enabled: bool = XenProperty(XenProperty.READONLY, 'true if HA is enabled on the pool, false otherwise')
    ha_host_failures_to_tolerate: int = XenProperty(XenProperty.READONLY, 'Number of host failures to tolerate before the Pool is declared to be overcommitted')
    ha_overcommitted: bool = XenProperty(XenProperty.READONLY, 'True if the Pool is considered to be overcommitted i.e. if there exist insufficient physical resources to tolerate the configured number of host failures')
    ha_plan_exists_for: int = XenProperty(XenProperty.READONLY, 'Number of future host failures we have managed to find a plan for. Once this reaches zero any future host failures will cause the failure of protected VMs.')
    ha_statefiles: List[str] = XenProperty(XenProperty.READONLY, 'HA statefile VDIs in use')
    health_check_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'Configuration for the automatic health check feature')
    igmp_snooping_enabled: bool = XenProperty(XenProperty.READONLY, 'true if IGMP snooping is enabled in the pool, false otherwise.')
    live_patching_disabled: bool = XenProperty(XenProperty.READWRITE, 'The pool-wide flag to show if the live patching feauture is disabled or not.')
    master: 'xenbridge.Host' = XenProperty(XenProperty.READONLY, 'The host that is pool master')
    metadata_VDIs: List['xenbridge.VDI'] = XenProperty(XenProperty.READONLY, 'The set of currently known metadata VDIs for this pool')
    name_description: str = XenProperty(XenProperty.READWRITE, 'Description')
    name_label: str = XenProperty(XenProperty.READWRITE, 'Short name')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    policy_no_vendor_device: bool = XenProperty(XenProperty.READWRITE, "The pool-wide policy for clients on whether to use the vendor device or not on newly created VMs. This field will also be consulted if the 'has_vendor_device' field is not specified in the VM.create call.")
    redo_log_enabled: bool = XenProperty(XenProperty.READONLY, 'true a redo-log is to be used other than when HA is enabled, false otherwise')
    redo_log_vdi: 'xenbridge.VDI' = XenProperty(XenProperty.READONLY, 'indicates the VDI to use for the redo-log other than when HA is enabled')
    restrictions: Dict[str, str] = XenProperty(XenProperty.READONLY, 'Pool-wide restrictions currently in effect')
    suspend_image_SR: 'xenbridge.SR' = XenProperty(XenProperty.READWRITE, 'The SR in which VDIs for suspend images are created')
    tags: List[str] = XenProperty(XenProperty.READWRITE, 'user-specified tags for categorization purposes')
    uefi_certificates: str = XenProperty(XenProperty.READWRITE, 'The UEFI certificates allowing Secure Boot')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')
    vswitch_controller: str = XenProperty(XenProperty.READONLY, 'address of the vswitch controller')
    wlb_enabled: bool = XenProperty(XenProperty.READWRITE, 'true if workload balancing is enabled on the pool, false otherwise')
    wlb_url: str = XenProperty(XenProperty.READONLY, 'Url for the configured workload balancing host')
    wlb_username: str = XenProperty(XenProperty.READONLY, 'Username for accessing the workload balancing host')
    wlb_verify_cert: bool = XenProperty(XenProperty.READWRITE, 'true if communication with the WLB server should enforce TLS certificate verification.')

    @XenMethod
    def add_tags(self, value: str) -> None:
        """Add the given value to the tags field of the given pool.  If the value is
        already in that Set, then do nothing."""
    @XenMethod
    def add_to_guest_agent_config(self, key: str, value: str) -> None:
        """Add a key-value pair to the pool-wide guest agent configuration"""
    @XenMethod
    def add_to_gui_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the gui_config field of the given pool."""
    @XenMethod
    def add_to_health_check_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the health_check_config field of the given pool."""
    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given pool."""
    @XenMethod
    def apply_edition(self, edition: str) -> None:
        """Apply an edition to all hosts in the pool"""
    @XenMethod
    def create_new_blob(self, name: str, mime_type: str, public: bool) -> 'xenbridge.Blob':
        """Create a placeholder for a named binary blob of data that is associated with
        this pool"""
    @XenMethod
    def detect_nonhomogeneous_external_auth(self) -> None:
        """This call asynchronously detects if the external authentication configuration in
        any slave is different from that in the master and raises appropriate alerts"""
    @XenMethod
    def disable_external_auth(self, config: Dict[str, str]) -> None:
        """This call disables external authentication on all the hosts of the pool"""
    @XenMethod
    def disable_local_storage_caching(self) -> None:
        """This call disables pool-wide local storage caching"""
    @XenMethod
    def disable_ssl_legacy(self) -> None:
        """Sets ssl_legacy false on each host, pool-master last. See Host.ssl_legacy and
        Host.set_ssl_legacy."""
    @XenMethod
    def enable_external_auth(self, config: Dict[str, str], service_name: str, auth_type: str) -> None:
        """This call enables external authentication on all the hosts of the pool"""
    @XenMethod
    def enable_local_storage_caching(self) -> None:
        """This call attempts to enable pool-wide local storage caching"""
    @XenMethod
    def enable_ssl_legacy(self) -> None:
        """Sets ssl_legacy true on each host, pool-master last. See Host.ssl_legacy and
        Host.set_ssl_legacy."""
    @XenMethod
    def get_license_state(self) -> Dict[str, str]:
        """This call returns the license state for the pool"""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given pool."""
    @XenMethod
    def has_extension(self, name: str) -> bool:
        """Return true if the extension is available on the pool"""
    @XenMethod
    def remove_from_guest_agent_config(self, key: str) -> None:
        """Remove a key-value pair from the pool-wide guest agent configuration"""
    @XenMethod
    def remove_from_gui_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the gui_config field of
        the given pool.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_from_health_check_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the health_check_config
        field of the given pool.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given pool.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_tags(self, value: str) -> None:
        """Remove the given value from the tags field of the given pool.  If the value is
        not in that Set, then do nothing."""
    @XenMethod
    def test_archive_target(self, config: Dict[str, str]) -> str:
        """This call tests if a location is valid"""


class PoolEndpoint(XenEndpoint):
    xenpath='pool'
    @XenMethod
    def certificate_install(self, name: str, cert: str) -> None:
        """Install a TLS CA certificate, pool-wide."""
    @XenMethod
    def certificate_list(self) -> List[str]:
        """List the names of all installed TLS CA certificates."""
    @XenMethod
    def certificate_sync(self) -> None:
        """Copy the TLS CA certificates and CRLs of the master to all slaves."""
    @XenMethod
    def certificate_uninstall(self, name: str) -> None:
        """Remove a pool-wide TLS CA certificate."""
    @XenMethod
    def create_VLAN(self, device: str, network: 'xenbridge.Network', VLAN: int) -> List['xenbridge.PIF']:
        """Create PIFs, mapping a network to the same physical interface/VLAN on each host.
        This call is deprecated: use Pool.create_VLAN_from_PIF instead."""
    @XenMethod
    def create_VLAN_from_PIF(self, pif: 'xenbridge.PIF', network: 'xenbridge.Network', VLAN: int) -> List['xenbridge.PIF']:
        """Create a pool-wide VLAN by taking the PIF."""
    @XenMethod
    def crl_install(self, name: str, cert: str) -> None:
        """Install a TLS Certificate Revocation List, pool-wide."""
    @XenMethod
    def crl_list(self) -> List[str]:
        """List the names of all installed TLS Certificate Revocation Lists."""
    @XenMethod
    def crl_uninstall(self, name: str) -> None:
        """Remove a pool-wide TLS Certificate Revocation List."""
    @XenMethod
    def deconfigure_wlb(self) -> None:
        """Permanently deconfigures workload balancing monitoring on this pool"""
    @XenMethod
    def designate_new_master(self, host: 'xenbridge.Host') -> None:
        """Perform an orderly handover of the role of master to the referenced host."""
    @XenMethod
    def disable_ha(self) -> None:
        """Turn off High Availability mode"""
    @XenMethod
    def disable_redo_log(self) -> None:
        """Disable the redo log if in use, unless HA is enabled."""
    @XenMethod
    def eject(self, host: 'xenbridge.Host') -> None:
        """Instruct a pool master to eject a host from the pool"""
    @XenMethod
    def emergency_reset_master(self, master_address: str) -> None:
        """Instruct a slave already in a pool that the master has changed"""
    @XenMethod
    def emergency_transition_to_master(self) -> None:
        """Instruct host that's currently a slave to transition to being master"""
    @XenMethod
    def enable_ha(self, heartbeat_srs: List['xenbridge.SR'], configuration: Dict[str, str]) -> None:
        """Turn on High Availability mode"""
    @XenMethod
    def enable_redo_log(self, sr: 'xenbridge.SR') -> None:
        """Enable the redo log on the given SR and start using it, unless HA is enabled."""
    @XenMethod
    def get_all(self) -> List['xenbridge.Pool']:
        """Return a list of all the pools known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.Pool', Dict[str, Any]]:
        """Return a map of pool references to pool records for all pools known to the
        system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.Pool':
        """Get a reference to the pool instance with the specified UUID."""
    @XenMethod
    def ha_compute_hypothetical_max_host_failures_to_tolerate(self, configuration: Dict['xenbridge.VM', str]) -> int:
        """Returns the maximum number of host failures we could tolerate before we would be
        unable to restart the provided VMs"""
    @XenMethod
    def ha_compute_max_host_failures_to_tolerate(self) -> int:
        """Returns the maximum number of host failures we could tolerate before we would be
        unable to restart configured VMs"""
    @XenMethod
    def ha_compute_vm_failover_plan(self, failed_hosts: List['xenbridge.Host'], failed_vms: List['xenbridge.VM']) -> Dict['xenbridge.VM', Dict[str, str]]:
        """Return a VM failover plan assuming a given subset of hosts fail"""
    @XenMethod
    def ha_failover_plan_exists(self, n: int) -> bool:
        """Returns true if a VM failover plan exists for up to 'n' host failures"""
    @XenMethod
    def ha_prevent_restarts_for(self, seconds: int) -> None:
        """When this call returns the VM restart logic will not run for the requested
        number of seconds. If the argument is zero then the restart thread is
        immediately unblocked"""
    @XenMethod
    def initialize_wlb(self, wlb_url: str, wlb_username: str, wlb_password: str, xenserver_username: str, xenserver_password: str) -> None:
        """Initializes workload balancing monitoring on this pool with the specified wlb
        server"""
    @XenMethod
    def join(self, master_address: str, master_username: str, master_password: str) -> None:
        """Instruct host to join a new pool"""
    @XenMethod
    def join_force(self, master_address: str, master_username: str, master_password: str) -> None:
        """Instruct host to join a new pool"""
    @XenMethod
    def management_reconfigure(self, network: 'xenbridge.Network') -> None:
        """Reconfigure the management network interface for all Hosts in the Pool"""
    @XenMethod
    def recover_slaves(self) -> List['xenbridge.Host']:
        """Instruct a pool master, M, to try and contact its slaves and, if slaves are in
        emergency mode, reset their master address to M."""
    @XenMethod
    def retrieve_wlb_configuration(self) -> Dict[str, str]:
        """Retrieves the pool optimization criteria from the workload balancing server"""
    @XenMethod
    def retrieve_wlb_recommendations(self) -> Dict['xenbridge.VM', List[str]]:
        """Retrieves vm migrate recommendations for the pool from the workload balancing
        server"""
    @XenMethod
    def send_test_post(self, host: str, port: int, body: str) -> str:
        """Send the given body to the given host and port, using HTTPS, and print the
        response.  This is used for debugging the SSL layer."""
    @XenMethod
    def send_wlb_configuration(self, config: Dict[str, str]) -> None:
        """Sets the pool optimization criteria for the workload balancing server"""
    @XenMethod
    def sync_database(self) -> None:
        """Forcibly synchronise the database now"""
