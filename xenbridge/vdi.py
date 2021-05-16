#Automatically generated from https://xapi-project.github.io/xen-api/classes/vdi.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class VdiOperations(XenEnum):
    CLONE = 'clone'
    COPY = 'copy'
    RESIZE = 'resize'
    RESIZE_ONLINE = 'resize_online'
    SNAPSHOT = 'snapshot'
    MIRROR = 'mirror'
    DESTROY = 'destroy'
    FORGET = 'forget'
    UPDATE = 'update'
    FORCE_UNLOCK = 'force_unlock'
    GENERATE_CONFIG = 'generate_config'
    ENABLE_CBT = 'enable_cbt'
    DISABLE_CBT = 'disable_cbt'
    DATA_DESTROY = 'data_destroy'
    LIST_CHANGED_BLOCKS = 'list_changed_blocks'
    SET_ON_BOOT = 'set_on_boot'
    BLOCKED = 'blocked'
class VdiType(XenEnum):
    SYSTEM = 'system'
    USER = 'user'
    EPHEMERAL = 'ephemeral'
    SUSPEND = 'suspend'
    CRASHDUMP = 'crashdump'
    HA_STATEFILE = 'ha_statefile'
    METADATA = 'metadata'
    REDO_LOG = 'redo_log'
    RRD = 'rrd'
    PVS_CACHE = 'pvs_cache'
    CBT_METADATA = 'cbt_metadata'
class OnBoot(XenEnum):
    RESET = 'reset'
    PERSIST = 'persist'

class VDI(XenObject):
    xenpath='VDI'

    SR: 'xenbridge.SR' = XenProperty(XenProperty.READONLY, 'storage repository in which the VDI resides')
    VBDs: List['xenbridge.VBD'] = XenProperty(XenProperty.READONLY, 'list of vbds that refer to this disk')
    allow_caching: bool = XenProperty(XenProperty.READONLY, 'true if this VDI is to be cached in the local cache SR')
    allowed_operations: List[VdiOperations] = XenProperty(XenProperty.READONLY, 'list of the operations allowed in this state. This list is advisory only and the server state may have changed by the time this field is read by a client.')
    cbt_enabled: bool = XenProperty(XenProperty.READONLY, 'True if changed blocks are tracked for this VDI')
    crash_dumps: List['xenbridge.Crashdump'] = XenProperty(XenProperty.READONLY, 'list of crash dumps that refer to this disk')
    current_operations: Dict[str, VdiOperations] = XenProperty(XenProperty.READONLY, 'links each of the running tasks using this object (by reference) to a current_operation enum which describes the nature of the task.')
    is_a_snapshot: bool = XenProperty(XenProperty.READONLY, 'true if this is a snapshot.')
    is_tools_iso: bool = XenProperty(XenProperty.READONLY, 'Whether this VDI is a Tools ISO')
    location: str = XenProperty(XenProperty.READONLY, 'location information')
    managed: bool = XenProperty(XenProperty.READONLY, '')
    metadata_latest: bool = XenProperty(XenProperty.READONLY, 'Whether this VDI contains the latest known accessible metadata for the pool')
    metadata_of_pool: 'xenbridge.Pool' = XenProperty(XenProperty.READONLY, 'The pool whose metadata is contained in this VDI')
    missing: bool = XenProperty(XenProperty.READONLY, 'true if SR scan operation reported this VDI as not present on disk')
    name_description: str = XenProperty(XenProperty.READONLY, 'a notes field containing human-readable description')
    name_label: str = XenProperty(XenProperty.READONLY, 'a human-readable name')
    on_boot: OnBoot = XenProperty(XenProperty.READONLY, 'The behaviour of this VDI on a VM boot')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    parent: 'xenbridge.VDI' = XenProperty(XenProperty.READONLY, 'This field is always null. Deprecated')
    physical_utilisation: int = XenProperty(XenProperty.READONLY, 'amount of physical space that the disk image is currently taking up on the storage repository (in bytes)')
    read_only: bool = XenProperty(XenProperty.READONLY, 'true if this disk may ONLY be mounted read-only')
    sharable: bool = XenProperty(XenProperty.READONLY, 'true if this disk may be shared')
    sm_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'SM dependent data')
    snapshot_of: 'xenbridge.VDI' = XenProperty(XenProperty.READONLY, 'Ref pointing to the VDI this snapshot is of.')
    snapshot_time: datetime.datetime = XenProperty(XenProperty.READONLY, 'Date/time when this snapshot was created.')
    snapshots: List['xenbridge.VDI'] = XenProperty(XenProperty.READONLY, 'List pointing to all the VDIs snapshots.')
    storage_lock: bool = XenProperty(XenProperty.READONLY, 'true if this disk is locked at the storage level')
    tags: List[str] = XenProperty(XenProperty.READWRITE, 'user-specified tags for categorization purposes')
    type: VdiType = XenProperty(XenProperty.READONLY, 'type of the VDI')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')
    virtual_size: int = XenProperty(XenProperty.READONLY, 'size of disk as presented to the guest (in bytes). Note that, depending on storage backend type, requested size may not be respected exactly')
    xenstore_data: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'data to be inserted into the xenstore tree (/local/domain/0/backend/vbd/<domid>/<device-id>/sm-data) after the VDI is attached. This is generally set by the SM backends on vdi_attach.')

    @XenMethod
    def add_tags(self, value: str) -> None:
        """Add the given value to the tags field of the given VDI.  If the value is already
        in that Set, then do nothing."""
    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given VDI."""
    @XenMethod
    def add_to_sm_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the sm_config field of the given VDI."""
    @XenMethod
    def add_to_xenstore_data(self, key: str, value: str) -> None:
        """Add the given key-value pair to the xenstore_data field of the given VDI."""
    @XenMethod
    def clone(self, driver_params: Dict[str, str]) -> 'xenbridge.VDI':
        """Take an exact copy of the VDI and return a reference to the new disk. If any
        driver_params are specified then these are passed through to the storage-
        specific substrate driver that implements the clone operation. NB the clone
        lives in the same Storage Repository as its parent."""
    @XenMethod
    def copy(self, sr: 'xenbridge.SR', base_vdi: 'xenbridge.VDI', into_vdi: 'xenbridge.VDI') -> 'xenbridge.VDI':
        """Copy either a full VDI or the block differences between two VDIs into either a
        fresh VDI or an existing VDI."""
    @XenMethod
    def data_destroy(self) -> None:
        """Delete the data of the snapshot VDI, but keep its changed block tracking
        metadata. When successful, this call changes the type of the VDI to
        cbt_metadata. This operation is idempotent: calling it on a VDI of type
        cbt_metadata results in a no-op, and no error will be thrown."""
    @XenMethod
    def destroy(self) -> None:
        """Destroy the specified VDI instance."""
    @XenMethod
    def disable_cbt(self) -> None:
        """Disable changed block tracking for the VDI. This call is only allowed on VDIs
        that support enabling CBT. It is an idempotent operation - disabling CBT for a
        VDI for which CBT is not enabled results in a no-op, and no error will be
        thrown."""
    @XenMethod
    def enable_cbt(self) -> None:
        """Enable changed block tracking for the VDI. This call is idempotent - enabling
        CBT for a VDI for which CBT is already enabled results in a no-op, and no error
        will be thrown."""
    @XenMethod
    def forget(self) -> None:
        """Removes a VDI record from the database"""
    @XenMethod
    def get_nbd_info(self) -> List[Dict[str, Any]]:
        """Get details specifying how to access this VDI via a Network Block Device server.
        For each of a set of NBD server addresses on which the VDI is available, the
        return value set contains a vdi_nbd_server_info object that contains an
        exportname to request once the NBD connection is established, and connection
        details for the address. An empty list is returned if there is no network that
        has a PIF on a host with access to the relevant SR, or if no such network has
        been assigned an NBD-related purpose in its purpose field. To access the given
        VDI, any of the vdi_nbd_server_info objects can be used to make a connection to
        a server, and then the VDI will be available by requesting the exportname."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given VDI."""
    @XenMethod
    def list_changed_blocks(self, vdi_to: 'xenbridge.VDI') -> str:
        """Compare two VDIs in 64k block increments and report which blocks differ. This
        operation is not allowed when vdi_to is attached to a VM."""
    @XenMethod
    def open_database(self) -> 'xenbridge.Session':
        """Load the metadata found on the supplied VDI and return a session reference which
        can be used in API calls to query its contents."""
    @XenMethod
    def pool_migrate(self, sr: 'xenbridge.SR', options: Dict[str, str]) -> 'xenbridge.VDI':
        """Migrate a VDI, which may be attached to a running guest, to a different SR. The
        destination SR must be visible to the guest."""
    @XenMethod
    def read_database_pool_uuid(self) -> str:
        """Check the VDI cache for the pool UUID of the database on this VDI."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given VDI.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_from_sm_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the sm_config field of the
        given VDI.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_from_xenstore_data(self, key: str) -> None:
        """Remove the given key and its corresponding value from the xenstore_data field of
        the given VDI.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_tags(self, value: str) -> None:
        """Remove the given value from the tags field of the given VDI.  If the value is
        not in that Set, then do nothing."""
    @XenMethod
    def resize(self, size: int) -> None:
        """Resize the VDI."""
    @XenMethod
    def resize_online(self, size: int) -> None:
        """Resize the VDI which may or may not be attached to running guests."""
    @XenMethod
    def snapshot(self, driver_params: Dict[str, str]) -> 'xenbridge.VDI':
        """Take a read-only snapshot of the VDI, returning a reference to the snapshot. If
        any driver_params are specified then these are passed through to the storage-
        specific substrate driver that takes the snapshot. NB the snapshot lives in the
        same Storage Repository as its parent."""
    @XenMethod
    def update(self) -> None:
        """Ask the storage backend to refresh the fields in the VDI object"""


class VDIEndpoint(XenEndpoint):
    xenpath='VDI'
    @XenMethod
    def create(self, args: Dict[str, Any]) -> 'xenbridge.VDI':
        """Create a new VDI instance, and return its handle. The constructor args are:
        name_label, name_description, SR*, virtual_size*, type*, sharable*, read_only*,
        other_config*, xenstore_data, sm_config, tags (* = non-optional)."""
    @XenMethod
    def get_all(self) -> List['xenbridge.VDI']:
        """Return a list of all the VDIs known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.VDI', Dict[str, Any]]:
        """Return a map of VDI references to VDI records for all VDIs known to the system."""
    @XenMethod
    def get_by_name_label(self, label: str) -> List['xenbridge.VDI']:
        """Get all the VDI instances with the given label."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.VDI':
        """Get a reference to the VDI instance with the specified UUID."""
    @XenMethod
    def introduce(self, uuid: str, name_label: str, name_description: str, SR: 'xenbridge.SR', type: VdiType, sharable: bool, read_only: bool, other_config: Dict[str, str], location: str, xenstore_data: Dict[str, str], sm_config: Dict[str, str], managed: bool, virtual_size: int, physical_utilisation: int, metadata_of_pool: 'xenbridge.Pool', is_a_snapshot: bool, snapshot_time: datetime.datetime, snapshot_of: 'xenbridge.VDI') -> 'xenbridge.VDI':
        """Create a new VDI record in the database only"""
