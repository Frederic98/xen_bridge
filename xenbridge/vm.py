#Automatically generated from https://xapi-project.github.io/xen-api/classes/vm.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class VmPowerState(XenEnum):
    HALTED = 'Halted'
    PAUSED = 'Paused'
    RUNNING = 'Running'
    SUSPENDED = 'Suspended'
class OnNormalExit(XenEnum):
    DESTROY = 'destroy'
    RESTART = 'restart'
class VmOperations(XenEnum):
    SNAPSHOT = 'snapshot'
    CLONE = 'clone'
    COPY = 'copy'
    CREATE_TEMPLATE = 'create_template'
    REVERT = 'revert'
    CHECKPOINT = 'checkpoint'
    SNAPSHOT_WITH_QUIESCE = 'snapshot_with_quiesce'
    PROVISION = 'provision'
    START = 'start'
    START_ON = 'start_on'
    PAUSE = 'pause'
    UNPAUSE = 'unpause'
    CLEAN_SHUTDOWN = 'clean_shutdown'
    CLEAN_REBOOT = 'clean_reboot'
    HARD_SHUTDOWN = 'hard_shutdown'
    POWER_STATE_RESET = 'power_state_reset'
    HARD_REBOOT = 'hard_reboot'
    SUSPEND = 'suspend'
    CSVM = 'csvm'
    RESUME = 'resume'
    RESUME_ON = 'resume_on'
    POOL_MIGRATE = 'pool_migrate'
    MIGRATE_SEND = 'migrate_send'
    GET_BOOT_RECORD = 'get_boot_record'
    SEND_SYSRQ = 'send_sysrq'
    SEND_TRIGGER = 'send_trigger'
    QUERY_SERVICES = 'query_services'
    SHUTDOWN = 'shutdown'
    CALL_PLUGIN = 'call_plugin'
    CHANGING_MEMORY_LIVE = 'changing_memory_live'
    AWAITING_MEMORY_LIVE = 'awaiting_memory_live'
    CHANGING_DYNAMIC_RANGE = 'changing_dynamic_range'
    CHANGING_STATIC_RANGE = 'changing_static_range'
    CHANGING_MEMORY_LIMITS = 'changing_memory_limits'
    CHANGING_SHADOW_MEMORY = 'changing_shadow_memory'
    CHANGING_SHADOW_MEMORY_LIVE = 'changing_shadow_memory_live'
    CHANGING_VCPUS = 'changing_VCPUs'
    CHANGING_VCPUS_LIVE = 'changing_VCPUs_live'
    CHANGING_NVRAM = 'changing_NVRAM'
    ASSERT_OPERATION_VALID = 'assert_operation_valid'
    DATA_SOURCE_OP = 'data_source_op'
    UPDATE_ALLOWED_OPERATIONS = 'update_allowed_operations'
    MAKE_INTO_TEMPLATE = 'make_into_template'
    IMPORT = 'import'
    EXPORT = 'export'
    METADATA_EXPORT = 'metadata_export'
    REVERTING = 'reverting'
    DESTROY = 'destroy'
class OnCrashBehaviour(XenEnum):
    DESTROY = 'destroy'
    COREDUMP_AND_DESTROY = 'coredump_and_destroy'
    RESTART = 'restart'
    COREDUMP_AND_RESTART = 'coredump_and_restart'
    PRESERVE = 'preserve'
    RENAME_RESTART = 'rename_restart'
class DomainType(XenEnum):
    HVM = 'hvm'
    PV = 'pv'
    PV_IN_PVH = 'pv_in_pvh'
    UNSPECIFIED = 'unspecified'

class VM(XenObject):
    xenpath='VM'

    HVM_boot_params: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'HVM boot params')
    HVM_boot_policy: str = XenProperty(XenProperty.READONLY, 'HVM boot policy')
    HVM_shadow_multiplier: float = XenProperty(XenProperty.READONLY, 'multiplier applied to the amount of shadow that will be made available to the guest')
    NVRAM: Dict[str, str] = XenProperty(XenProperty.READONLY, 'initial value for guest NVRAM (containing UEFI variables, etc). Cannot be changed while the VM is running')
    PCI_bus: str = XenProperty(XenProperty.READWRITE, 'PCI bus path for pass-through devices')
    PV_args: str = XenProperty(XenProperty.READWRITE, 'kernel command-line arguments')
    PV_bootloader: str = XenProperty(XenProperty.READWRITE, 'name of or path to bootloader')
    PV_bootloader_args: str = XenProperty(XenProperty.READWRITE, 'miscellaneous arguments for the bootloader')
    PV_kernel: str = XenProperty(XenProperty.READWRITE, 'path to the kernel')
    PV_legacy_args: str = XenProperty(XenProperty.READWRITE, 'to make Zurich guests boot')
    PV_ramdisk: str = XenProperty(XenProperty.READWRITE, 'path to the initrd')
    VBDs: List['xenbridge.VBD'] = XenProperty(XenProperty.READONLY, 'virtual block devices')
    VCPUs_at_startup: int = XenProperty(XenProperty.READONLY, 'Boot number of VCPUs')
    VCPUs_max: int = XenProperty(XenProperty.READONLY, 'Max number of VCPUs')
    VCPUs_params: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'configuration parameters for the selected VCPU policy')
    VGPUs: List['xenbridge.VGPU'] = XenProperty(XenProperty.READONLY, 'Virtual GPUs')
    VIFs: List['xenbridge.VIF'] = XenProperty(XenProperty.READONLY, 'virtual network interfaces')
    VTPMs: List['xenbridge.VTPM'] = XenProperty(XenProperty.READONLY, 'virtual TPMs')
    VUSBs: List['xenbridge.VUSB'] = XenProperty(XenProperty.READONLY, 'vitual usb devices')
    actions_after_crash: OnCrashBehaviour = XenProperty(XenProperty.READONLY, 'action to take if the guest crashes')
    actions_after_reboot: OnNormalExit = XenProperty(XenProperty.READWRITE, 'action to take after the guest has rebooted itself')
    actions_after_shutdown: OnNormalExit = XenProperty(XenProperty.READWRITE, 'action to take after the guest has shutdown itself')
    affinity: 'xenbridge.Host' = XenProperty(XenProperty.READWRITE, 'A host which the VM has some affinity for (or NULL). This is used as a hint to the start call when it decides where to run the VM. Resource constraints may cause the VM to be started elsewhere.')
    allowed_operations: List[VmOperations] = XenProperty(XenProperty.READONLY, 'list of the operations allowed in this state. This list is advisory only and the server state may have changed by the time this field is read by a client.')
    appliance: 'xenbridge.VMAppliance' = XenProperty(XenProperty.READONLY, 'the appliance to which this VM belongs')
    attached_PCIs: List['xenbridge.PCI'] = XenProperty(XenProperty.READONLY, 'Currently passed-through PCI devices')
    bios_strings: Dict[str, str] = XenProperty(XenProperty.READONLY, 'BIOS strings')
    blobs: Dict[str, 'xenbridge.Blob'] = XenProperty(XenProperty.READONLY, 'Binary blobs associated with this VM')
    blocked_operations: Dict[VmOperations, str] = XenProperty(XenProperty.READWRITE, 'List of operations which have been explicitly blocked and an error code')
    children: List['xenbridge.VM'] = XenProperty(XenProperty.READONLY, 'List pointing to all the children of this VM')
    consoles: List['xenbridge.Console'] = XenProperty(XenProperty.READONLY, 'virtual console devices')
    crash_dumps: List['xenbridge.Crashdump'] = XenProperty(XenProperty.READONLY, 'crash dumps associated with this VM')
    current_operations: Dict[str, VmOperations] = XenProperty(XenProperty.READONLY, 'links each of the running tasks using this object (by reference) to a current_operation enum which describes the nature of the task.')
    domain_type: DomainType = XenProperty(XenProperty.READONLY, 'The type of domain that will be created when the VM is started')
    domarch: str = XenProperty(XenProperty.READONLY, 'Domain architecture (if available, null string otherwise)')
    domid: int = XenProperty(XenProperty.READONLY, 'domain ID (if available, -1 otherwise)')
    generation_id: str = XenProperty(XenProperty.READONLY, 'Generation ID of the VM')
    guest_metrics: 'xenbridge.VMGuestMetrics' = XenProperty(XenProperty.READONLY, 'metrics associated with the running guest')
    ha_always_run: bool = XenProperty(XenProperty.READONLY, 'if true then the system will attempt to keep the VM running as much as possible.')
    ha_restart_priority: str = XenProperty(XenProperty.READONLY, 'has possible values: "best-effort" meaning "try to restart this VM if possible but don\'t consider the Pool to be overcommitted if this is not possible"; "restart" meaning "this VM should be restarted"; "" meaning "do not try to restart this VM"')
    hardware_platform_version: int = XenProperty(XenProperty.READWRITE, 'The host virtual hardware platform version the VM can run on')
    has_vendor_device: bool = XenProperty(XenProperty.READONLY, 'When an HVM guest starts, this controls the presence of the emulated C000 PCI device which triggers Windows Update to fetch or update PV drivers.')
    is_a_snapshot: bool = XenProperty(XenProperty.READONLY, 'true if this is a snapshot. Snapshotted VMs can never be started, they are used only for cloning other VMs')
    is_a_template: bool = XenProperty(XenProperty.READWRITE, 'true if this is a template. Template VMs can never be started, they are used only for cloning other VMs')
    is_control_domain: bool = XenProperty(XenProperty.READONLY, 'true if this is a control domain (domain 0 or a driver domain)')
    is_default_template: bool = XenProperty(XenProperty.READONLY, 'true if this is a default template. Default template VMs can never be started or migrated, they are used only for cloning other VMs')
    is_snapshot_from_vmpp: bool = XenProperty(XenProperty.READONLY, 'true if this snapshot was created by the protection policy')
    is_vmss_snapshot: bool = XenProperty(XenProperty.READONLY, 'true if this snapshot was created by the snapshot schedule')
    last_boot_CPU_flags: Dict[str, str] = XenProperty(XenProperty.READONLY, 'describes the CPU flags on which the VM was last booted')
    last_booted_record: str = XenProperty(XenProperty.READONLY, 'marshalled value containing VM record at time of last boot')
    memory_dynamic_max: int = XenProperty(XenProperty.READONLY, 'Dynamic maximum (bytes)')
    memory_dynamic_min: int = XenProperty(XenProperty.READONLY, 'Dynamic minimum (bytes)')
    memory_overhead: int = XenProperty(XenProperty.READONLY, 'The VM.memory_* fields describe how much virtual RAM the\nVM can see. Every running VM requires extra host memory to store\nthings like\n\nshadow copies of page tables, needed during migration or\nif hardware assisted paging is not available\nvideo RAM for the virtual graphics card\nrecords in the hypervisor describing the VM and the vCPUs\n\nThese memory "overheads" are recomputed every time the VM\'s\nconfiguration changes, and the result is stored in\nVM.memory_overhead.\nFor more information, read about\nHost memory accounting')
    memory_static_max: int = XenProperty(XenProperty.READONLY, 'Statically-set (i.e. absolute) maximum (bytes). The value of this field at VM start time acts as a hard limit of the amount of memory a guest can use. New values only take effect on reboot.')
    memory_static_min: int = XenProperty(XenProperty.READONLY, 'Statically-set (i.e. absolute) mininum (bytes). The value of this field indicates the least amount of memory this VM can boot with without crashing.')
    memory_target: int = XenProperty(XenProperty.READONLY, 'Dynamically-set memory target (bytes). The value of this field indicates the current target for memory available to this VM.')
    metrics: 'xenbridge.VMMetrics' = XenProperty(XenProperty.READONLY, 'metrics associated with this VM')
    name_description: str = XenProperty(XenProperty.READWRITE, 'a notes field containing human-readable description')
    name_label: str = XenProperty(XenProperty.READWRITE, 'a human-readable name')
    order: int = XenProperty(XenProperty.READONLY, 'The point in the startup or shutdown sequence at which this VM will be started')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    parent: 'xenbridge.VM' = XenProperty(XenProperty.READONLY, 'Ref pointing to the parent of this VM')
    platform: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'platform-specific configuration')
    power_state: VmPowerState = XenProperty(XenProperty.READONLY, 'Current power state of the machine')
    protection_policy: 'xenbridge.VMPP' = XenProperty(XenProperty.READONLY, 'Ref pointing to a protection policy for this VM')
    recommendations: str = XenProperty(XenProperty.READWRITE, 'An XML specification of recommended values and ranges for properties of this VM')
    reference_label: str = XenProperty(XenProperty.READONLY, "Textual reference to the template used to create a VM. This can be used by clients in need of an immutable reference to the template since the latter's uuid and name_label may change, for example, after a package installation or upgrade.")
    requires_reboot: bool = XenProperty(XenProperty.READONLY, 'Indicates whether a VM requires a reboot in order to update its configuration, e.g. its memory allocation.')
    resident_on: 'xenbridge.Host' = XenProperty(XenProperty.READONLY, 'the host the VM is currently resident on')
    scheduled_to_be_resident_on: 'xenbridge.Host' = XenProperty(XenProperty.READONLY, 'the host on which the VM is due to be started/resumed/migrated. This acts as a memory reservation indicator')
    shutdown_delay: int = XenProperty(XenProperty.READONLY, 'The delay to wait before proceeding to the next order in the shutdown sequence (seconds)')
    snapshot_info: Dict[str, str] = XenProperty(XenProperty.READONLY, 'Human-readable information concerning this snapshot')
    snapshot_metadata: str = XenProperty(XenProperty.READONLY, "Encoded information about the VM's metadata this is a snapshot of")
    snapshot_of: 'xenbridge.VM' = XenProperty(XenProperty.READONLY, 'Ref pointing to the VM this snapshot is of.')
    snapshot_schedule: 'xenbridge.VMSS' = XenProperty(XenProperty.READONLY, 'Ref pointing to a snapshot schedule for this VM')
    snapshot_time: datetime.datetime = XenProperty(XenProperty.READONLY, 'Date/time when this snapshot was created.')
    snapshots: List['xenbridge.VM'] = XenProperty(XenProperty.READONLY, 'List pointing to all the VM snapshots.')
    start_delay: int = XenProperty(XenProperty.READONLY, 'The delay to wait before proceeding to the next order in the startup sequence (seconds)')
    suspend_SR: 'xenbridge.SR' = XenProperty(XenProperty.READWRITE, 'The SR on which a suspend image is stored')
    suspend_VDI: 'xenbridge.VDI' = XenProperty(XenProperty.READONLY, 'The VDI that a suspend image is stored on. (Only has meaning if VM is currently suspended)')
    tags: List[str] = XenProperty(XenProperty.READWRITE, 'user-specified tags for categorization purposes')
    transportable_snapshot_id: str = XenProperty(XenProperty.READONLY, 'Transportable ID of the snapshot VM')
    user_version: int = XenProperty(XenProperty.READWRITE, 'Creators of VMs and templates may store version information here.')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')
    version: int = XenProperty(XenProperty.READONLY, 'The number of times this VM has been recovered')
    xenstore_data: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'data to be inserted into the xenstore tree (/local/domain/<domid>/vm-data) after the VM is created.')

    @XenMethod
    def add_tags(self, value: str) -> None:
        """Add the given value to the tags field of the given VM.  If the value is already
        in that Set, then do nothing."""
    @XenMethod
    def add_to_HVM_boot_params(self, key: str, value: str) -> None:
        """Add the given key-value pair to the HVM/boot_params field of the given VM."""
    @XenMethod
    def add_to_NVRAM(self, key: str, value: str) -> None:
        ...
    @XenMethod
    def add_to_VCPUs_params(self, key: str, value: str) -> None:
        """Add the given key-value pair to the VCPUs/params field of the given VM."""
    @XenMethod
    def add_to_VCPUs_params_live(self, key: str, value: str) -> None:
        """Add the given key-value pair to VM.VCPUs_params, and apply that value on the
        running VM"""
    @XenMethod
    def add_to_blocked_operations(self, key: VmOperations, value: str) -> None:
        """Add the given key-value pair to the blocked_operations field of the given VM."""
    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given VM."""
    @XenMethod
    def add_to_platform(self, key: str, value: str) -> None:
        """Add the given key-value pair to the platform field of the given VM."""
    @XenMethod
    def add_to_xenstore_data(self, key: str, value: str) -> None:
        """Add the given key-value pair to the xenstore_data field of the given VM."""
    @XenMethod
    def assert_agile(self) -> None:
        """Returns an error if the VM is not considered agile e.g. because it is tied to a
        resource local to a host"""
    @XenMethod
    def assert_can_be_recovered(self, session_to: 'xenbridge.Session') -> None:
        """Assert whether all SRs required to recover this VM are available."""
    @XenMethod
    def assert_can_boot_here(self, host: 'xenbridge.Host') -> None:
        """Returns an error if the VM could not boot on this host for some reason"""
    @XenMethod
    def assert_can_migrate(self, dest: Dict[str, str], live: bool, vdi_map: Dict['xenbridge.VDI', 'xenbridge.SR'], vif_map: Dict['xenbridge.VIF', 'xenbridge.Network'], options: Dict[str, str], vgpu_map: Dict['xenbridge.VGPU', 'xenbridge.GPUGroup']) -> None:
        """Assert whether a VM can be migrated to the specified destination."""
    @XenMethod
    def assert_operation_valid(self, op: VmOperations) -> None:
        """Check to see whether this operation is acceptable in the current state of the
        system, raising an error if the operation is invalid for some reason"""
    @XenMethod
    def call_plugin(self, plugin: str, fn: str, args: Dict[str, str]) -> str:
        """Call an API plugin on this vm"""
    @XenMethod
    def checkpoint(self, new_name: str) -> 'xenbridge.VM':
        """Checkpoints the specified VM, making a new VM. Checkpoint automatically exploits
        the capabilities of the underlying storage repository in which the VM's disk
        images are stored (e.g. Copy on Write) and saves the memory image as well."""
    @XenMethod
    def clean_reboot(self) -> None:
        """Attempt to cleanly shutdown the specified VM (Note: this may not be supported---
        e.g. if a guest agent is not installed). This can only be called when the
        specified VM is in the Running state."""
    @XenMethod
    def clean_shutdown(self) -> None:
        """Attempt to cleanly shutdown the specified VM. (Note: this may not be supported
        ---e.g. if a guest agent is not installed). This can only be called when the
        specified VM is in the Running state."""
    @XenMethod
    def clone(self, new_name: str) -> 'xenbridge.VM':
        """Clones the specified VM, making a new VM. Clone automatically exploits the
        capabilities of the underlying storage repository in which the VM's disk images
        are stored (e.g. Copy on Write).   This function can only be called when the VM
        is in the Halted State."""
    @XenMethod
    def compute_memory_overhead(self) -> int:
        """Computes the virtualization memory overhead of a VM."""
    @XenMethod
    def copy(self, new_name: str, sr: 'xenbridge.SR') -> 'xenbridge.VM':
        """Copied the specified VM, making a new VM. Unlike clone, copy does not exploits
        the capabilities of the underlying storage repository in which the VM's disk
        images are stored. Instead, copy guarantees that the disk images of the newly
        created VM will be 'full disks' - i.e. not part of a CoW chain.  This function
        can only be called when the VM is in the Halted State."""
    @XenMethod
    def copy_bios_strings(self, host: 'xenbridge.Host') -> None:
        """Copy the BIOS strings from the given host to this VM"""
    @XenMethod
    def create_new_blob(self, name: str, mime_type: str, public: bool) -> 'xenbridge.Blob':
        """Create a placeholder for a named binary blob of data that is associated with
        this VM"""
    @XenMethod
    def destroy(self) -> None:
        """Destroy the specified VM.  The VM is completely removed from the system.  This
        function can only be called when the VM is in the Halted State."""
    @XenMethod
    def forget_data_source_archives(self, data_source: str) -> None:
        """Forget the recorded statistics related to the specified data source"""
    @XenMethod
    def get_SRs_required_for_recovery(self, session_to: 'xenbridge.Session') -> List['xenbridge.SR']:
        """List all the SR's that are required for the VM to be recovered"""
    @XenMethod
    def get_allowed_VBD_devices(self) -> List[str]:
        """Returns a list of the allowed values that a VBD device field can take"""
    @XenMethod
    def get_allowed_VIF_devices(self) -> List[str]:
        """Returns a list of the allowed values that a VIF device field can take"""
    @XenMethod
    def get_boot_record(self) -> Dict[str, Any]:
        """Returns a record describing the VM's dynamic state, initialised when the VM
        boots and updated to reflect runtime configuration changes e.g. CPU hotplug"""
    @XenMethod
    def get_cooperative(self) -> bool:
        """Return true if the VM is currently 'co-operative' i.e. is expected to reach a
        balloon target and actually has done"""
    @XenMethod
    def get_data_sources(self) -> List[Dict[str, Any]]:
        ...
    @XenMethod
    def get_possible_hosts(self) -> List['xenbridge.Host']:
        """Return the list of hosts on which this VM may run."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given VM."""
    @XenMethod
    def hard_reboot(self) -> None:
        """Stop executing the specified VM without attempting a clean shutdown and
        immediately restart the VM."""
    @XenMethod
    def hard_shutdown(self) -> None:
        """Stop executing the specified VM without attempting a clean shutdown."""
    @XenMethod
    def maximise_memory(self, total: int, approximate: bool) -> int:
        """Returns the maximum amount of guest memory which will fit, together with
        overheads, in the supplied amount of physical memory. If 'exact' is true then an
        exact calculation is performed using the VM's current settings. If 'exact' is
        false then a more conservative approximation is used"""
    @XenMethod
    def migrate_send(self, dest: Dict[str, str], live: bool, vdi_map: Dict['xenbridge.VDI', 'xenbridge.SR'], vif_map: Dict['xenbridge.VIF', 'xenbridge.Network'], options: Dict[str, str], vgpu_map: Dict['xenbridge.VGPU', 'xenbridge.GPUGroup']) -> 'xenbridge.VM':
        """Migrate the VM to another host.  This can only be called when the specified VM
        is in the Running state."""
    @XenMethod
    def pause(self) -> None:
        """Pause the specified VM. This can only be called when the specified VM is in the
        Running state."""
    @XenMethod
    def pool_migrate(self, host: 'xenbridge.Host', options: Dict[str, str]) -> None:
        """Migrate a VM to another Host."""
    @XenMethod
    def power_state_reset(self) -> None:
        """Reset the power-state of the VM to halted in the database only. (Used to recover
        from slave failures in pooling scenarios by resetting the power-states of VMs
        running on dead slaves to halted.) This is a potentially dangerous operation;
        use with care."""
    @XenMethod
    def provision(self) -> None:
        """Inspects the disk configuration contained within the VM's other_config, creates
        VDIs and VBDs and then executes any applicable post-install script."""
    @XenMethod
    def query_data_source(self, data_source: str) -> float:
        """Query the latest value of the specified data source"""
    @XenMethod
    def query_services(self) -> Dict[str, str]:
        """Query the system services advertised by this VM and register them. This can only
        be applied to a system domain."""
    @XenMethod
    def record_data_source(self, data_source: str) -> None:
        """Start recording the specified data source"""
    @XenMethod
    def recover(self, session_to: 'xenbridge.Session', force: bool) -> None:
        """Recover the VM"""
    @XenMethod
    def remove_from_HVM_boot_params(self, key: str) -> None:
        """Remove the given key and its corresponding value from the HVM/boot_params field
        of the given VM.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_from_NVRAM(self, key: str) -> None:
        ...
    @XenMethod
    def remove_from_VCPUs_params(self, key: str) -> None:
        """Remove the given key and its corresponding value from the VCPUs/params field of
        the given VM.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_from_blocked_operations(self, key: VmOperations) -> None:
        """Remove the given key and its corresponding value from the blocked_operations
        field of the given VM.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given VM.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_from_platform(self, key: str) -> None:
        """Remove the given key and its corresponding value from the platform field of the
        given VM.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_from_xenstore_data(self, key: str) -> None:
        """Remove the given key and its corresponding value from the xenstore_data field of
        the given VM.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_tags(self, value: str) -> None:
        """Remove the given value from the tags field of the given VM.  If the value is not
        in that Set, then do nothing."""
    @XenMethod
    def resume(self, start_paused: bool, force: bool) -> None:
        """Awaken the specified VM and resume it.  This can only be called when the
        specified VM is in the Suspended state."""
    @XenMethod
    def resume_on(self, host: 'xenbridge.Host', start_paused: bool, force: bool) -> None:
        """Awaken the specified VM and resume it on a particular Host.  This can only be
        called when the specified VM is in the Suspended state."""
    @XenMethod
    def retrieve_wlb_recommendations(self) -> Dict['xenbridge.Host', List[str]]:
        """Returns mapping of hosts to ratings, indicating the suitability of starting the
        VM at that location according to wlb. Rating is replaced with an error if the VM
        cannot boot there."""
    @XenMethod
    def revert(self) -> None:
        """Reverts the specified VM to a previous state."""
    @XenMethod
    def send_sysrq(self, key: str) -> None:
        """Send the given key as a sysrq to this VM.  The key is specified as a single
        character (a String of length 1).  This can only be called when the specified VM
        is in the Running state."""
    @XenMethod
    def send_trigger(self, trigger: str) -> None:
        """Send the named trigger to this VM.  This can only be called when the specified
        VM is in the Running state."""
    @XenMethod
    def set_VCPUs_number_live(self, nvcpu: int) -> None:
        """Set the number of VCPUs for a running VM"""
    @XenMethod
    def set_memory(self, value: int) -> None:
        """Set the memory allocation of this VM. Sets all of memory_static_max,
        memory_dynamic_min, and memory_dynamic_max to the given value, and leaves
        memory_static_min untouched."""
    @XenMethod
    def set_memory_dynamic_range(self, min: int, max: int) -> None:
        """Set the minimum and maximum amounts of physical memory the VM is allowed to use."""
    @XenMethod
    def set_memory_limits(self, static_min: int, static_max: int, dynamic_min: int, dynamic_max: int) -> None:
        """Set the memory limits of this VM."""
    @XenMethod
    def set_memory_static_range(self, min: int, max: int) -> None:
        """Set the static (ie boot-time) range of virtual memory that the VM is allowed to
        use."""
    @XenMethod
    def set_memory_target_live(self, target: int) -> None:
        """Set the memory target for a running VM"""
    @XenMethod
    def set_shadow_multiplier_live(self, multiplier: float) -> None:
        """Set the shadow memory multiplier on a running VM"""
    @XenMethod
    def shutdown(self) -> None:
        """Attempts to first clean shutdown a VM and if it should fail then perform a hard
        shutdown on it."""
    @XenMethod
    def snapshot(self, new_name: str) -> 'xenbridge.VM':
        """Snapshots the specified VM, making a new VM. Snapshot automatically exploits the
        capabilities of the underlying storage repository in which the VM's disk images
        are stored (e.g. Copy on Write)."""
    @XenMethod
    def snapshot_with_quiesce(self, new_name: str) -> 'xenbridge.VM':
        """Snapshots the specified VM with quiesce, making a new VM. Snapshot automatically
        exploits the capabilities of the underlying storage repository in which the VM's
        disk images are stored (e.g. Copy on Write)."""
    @XenMethod
    def start(self, start_paused: bool, force: bool) -> None:
        """Start the specified VM.  This function can only be called with the VM is in the
        Halted State."""
    @XenMethod
    def start_on(self, host: 'xenbridge.Host', start_paused: bool, force: bool) -> None:
        """Start the specified VM on a particular host.  This function can only be called
        with the VM is in the Halted State."""
    @XenMethod
    def suspend(self) -> None:
        """Suspend the specified VM to disk.  This can only be called when the specified VM
        is in the Running state."""
    @XenMethod
    def unpause(self) -> None:
        """Resume the specified VM. This can only be called when the specified VM is in the
        Paused state."""
    @XenMethod
    def update_allowed_operations(self) -> None:
        """Recomputes the list of acceptable operations"""
    @XenMethod
    def wait_memory_target_live(self) -> None:
        """Wait for a running VM to reach its current memory target"""


class VMEndpoint(XenEndpoint):
    xenpath='VM'
    @XenMethod
    def create(self, args: Dict[str, Any]) -> 'xenbridge.VM':
        """NOT RECOMMENDED! VM.clone or VM.copy (or VM.import) is a better choice in almost
        all situations. The standard way to obtain a new VM is to call VM.clone on a
        template VM, then call VM.provision on the new clone. Caution: if VM.create is
        used and then the new VM is attached to a virtual disc that has an operating
        system already installed, then there is no guarantee that the operating system
        will boot and run. Any software that calls VM.create on a future version of this
        API may fail or give unexpected results. For example this could happen if an
        additional parameter were added to VM.create. VM.create is intended only for use
        in the automatic creation of the system VM templates. It creates a new VM
        instance, and returns its handle. The constructor args are: name_label,
        name_description, power_state, user_version*, is_a_template*, suspend_VDI,
        affinity*, memory_target, memory_static_max*, memory_dynamic_max*,
        memory_dynamic_min*, memory_static_min*, VCPUs_params*, VCPUs_max*,
        VCPUs_at_startup*, actions_after_shutdown*, actions_after_reboot*,
        actions_after_crash*, PV_bootloader*, PV_kernel*, PV_ramdisk*, PV_args*,
        PV_bootloader_args*, PV_legacy_args*, HVM_boot_policy*, HVM_boot_params*,
        HVM_shadow_multiplier, platform*, PCI_bus*, other_config*, last_boot_CPU_flags,
        last_booted_record, recommendations*, xenstore_data, ha_always_run,
        ha_restart_priority, tags, blocked_operations, protection_policy,
        is_snapshot_from_vmpp, snapshot_schedule, is_vmss_snapshot, appliance,
        start_delay, shutdown_delay, order, suspend_SR, version, generation_id,
        hardware_platform_version, has_vendor_device, reference_label, domain_type,
        NVRAM (* = non-optional)."""
    @XenMethod
    def get_all(self) -> List['xenbridge.VM']:
        """Return a list of all the VMs known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.VM', Dict[str, Any]]:
        """Return a map of VM references to VM records for all VMs known to the system."""
    @XenMethod
    def get_by_name_label(self, label: str) -> List['xenbridge.VM']:
        """Get all the VM instances with the given label."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.VM':
        """Get a reference to the VM instance with the specified UUID."""
    @XenMethod
    def import_(self, url: str, sr: 'xenbridge.SR', full_restore: bool, force: bool) -> List['xenbridge.VM']:
        """Import an XVA from a URI"""
    @XenMethod
    def import_convert(self, type: str, username: str, password: str, sr: 'xenbridge.SR', remote_config: Dict[str, str]) -> None:
        """Import using a conversion service."""
