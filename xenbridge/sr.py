#Automatically generated from https://xapi-project.github.io/xen-api/classes/sr.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class StorageOperations(XenEnum):
    SCAN = 'scan'
    DESTROY = 'destroy'
    FORGET = 'forget'
    PLUG = 'plug'
    UNPLUG = 'unplug'
    UPDATE = 'update'
    VDI_CREATE = 'vdi_create'
    VDI_INTRODUCE = 'vdi_introduce'
    VDI_DESTROY = 'vdi_destroy'
    VDI_RESIZE = 'vdi_resize'
    VDI_CLONE = 'vdi_clone'
    VDI_SNAPSHOT = 'vdi_snapshot'
    VDI_MIRROR = 'vdi_mirror'
    VDI_ENABLE_CBT = 'vdi_enable_cbt'
    VDI_DISABLE_CBT = 'vdi_disable_cbt'
    VDI_DATA_DESTROY = 'vdi_data_destroy'
    VDI_LIST_CHANGED_BLOCKS = 'vdi_list_changed_blocks'
    VDI_SET_ON_BOOT = 'vdi_set_on_boot'
    PBD_CREATE = 'pbd_create'
    PBD_DESTROY = 'pbd_destroy'

class SR(XenObject):
    xenpath='SR'

    PBDs: List['xenbridge.PBD'] = XenProperty(XenProperty.READONLY, 'describes how particular hosts can see this storage repository')
    VDIs: List['xenbridge.VDI'] = XenProperty(XenProperty.READONLY, 'all virtual disks known to this storage repository')
    allowed_operations: List[StorageOperations] = XenProperty(XenProperty.READONLY, 'list of the operations allowed in this state. This list is advisory only and the server state may have changed by the time this field is read by a client.')
    blobs: Dict[str, 'xenbridge.Blob'] = XenProperty(XenProperty.READONLY, 'Binary blobs associated with this SR')
    clustered: bool = XenProperty(XenProperty.READONLY, 'True if the SR is using aggregated local storage')
    content_type: str = XenProperty(XenProperty.READONLY, "the type of the SR's content, if required (e.g. ISOs)")
    current_operations: Dict[str, StorageOperations] = XenProperty(XenProperty.READONLY, 'links each of the running tasks using this object (by reference) to a current_operation enum which describes the nature of the task.')
    introduced_by: 'xenbridge.DRTask' = XenProperty(XenProperty.READONLY, 'The disaster recovery task which introduced this SR')
    is_tools_sr: bool = XenProperty(XenProperty.READONLY, 'True if this is the SR that contains the Tools ISO VDIs')
    local_cache_enabled: bool = XenProperty(XenProperty.READONLY, 'True if this SR is assigned to be the local cache for its host')
    name_description: str = XenProperty(XenProperty.READONLY, 'a notes field containing human-readable description')
    name_label: str = XenProperty(XenProperty.READONLY, 'a human-readable name')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    physical_size: int = XenProperty(XenProperty.READONLY, 'total physical size of the repository (in bytes)')
    physical_utilisation: int = XenProperty(XenProperty.READONLY, 'physical space currently utilised on this storage repository (in bytes). Note that for sparse disk formats, physical_utilisation may be less than virtual_allocation')
    shared: bool = XenProperty(XenProperty.READONLY, 'true if this SR is (capable of being) shared between multiple hosts')
    sm_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'SM dependent data')
    tags: List[str] = XenProperty(XenProperty.READWRITE, 'user-specified tags for categorization purposes')
    type: str = XenProperty(XenProperty.READONLY, 'type of the storage repository')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')
    virtual_allocation: int = XenProperty(XenProperty.READONLY, 'sum of virtual_sizes of all VDIs in this storage repository (in bytes)')

    @XenMethod
    def add_tags(self, value: str) -> None:
        """Add the given value to the tags field of the given SR.  If the value is already
        in that Set, then do nothing."""
    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given SR."""
    @XenMethod
    def add_to_sm_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the sm_config field of the given SR."""
    @XenMethod
    def assert_can_host_ha_statefile(self) -> None:
        """Returns successfully if the given SR can host an HA statefile. Otherwise returns
        an error to explain why not"""
    @XenMethod
    def assert_supports_database_replication(self) -> None:
        """Returns successfully if the given SR supports database replication. Otherwise
        returns an error to explain why not."""
    @XenMethod
    def create_new_blob(self, name: str, mime_type: str, public: bool) -> 'xenbridge.Blob':
        """Create a placeholder for a named binary blob of data that is associated with
        this SR"""
    @XenMethod
    def destroy(self) -> None:
        """Destroy specified SR, removing SR-record from database and remove SR from disk.
        (In order to affect this operation the appropriate device_config is read from
        the specified SR's PBD on current host)"""
    @XenMethod
    def disable_database_replication(self) -> None:
        ...
    @XenMethod
    def enable_database_replication(self) -> None:
        ...
    @XenMethod
    def forget(self) -> None:
        """Removing specified SR-record from database, without attempting to remove SR from
        disk"""
    @XenMethod
    def forget_data_source_archives(self, data_source: str) -> None:
        """Forget the recorded statistics related to the specified data source"""
    @XenMethod
    def get_data_sources(self) -> List[Dict[str, Any]]:
        ...
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given SR."""
    @XenMethod
    def query_data_source(self, data_source: str) -> float:
        """Query the latest value of the specified data source"""
    @XenMethod
    def record_data_source(self, data_source: str) -> None:
        """Start recording the specified data source"""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given SR.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_from_sm_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the sm_config field of the
        given SR.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_tags(self, value: str) -> None:
        """Remove the given value from the tags field of the given SR.  If the value is not
        in that Set, then do nothing."""
    @XenMethod
    def scan(self) -> None:
        """Refreshes the list of VDIs associated with an SR"""
    @XenMethod
    def update(self) -> None:
        """Refresh the fields on the SR object"""


class SREndpoint(XenEndpoint):
    xenpath='SR'
    @XenMethod
    def create(self, host: 'xenbridge.Host', device_config: Dict[str, str], physical_size: int, name_label: str, name_description: str, type: str, content_type: str, shared: bool, sm_config: Dict[str, str]) -> 'xenbridge.SR':
        """Create a new Storage Repository and introduce it into the managed system,
        creating both SR record and PBD record to attach it to current host (with
        specified device_config parameters)"""
    @XenMethod
    def get_all(self) -> List['xenbridge.SR']:
        """Return a list of all the SRs known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.SR', Dict[str, Any]]:
        """Return a map of SR references to SR records for all SRs known to the system."""
    @XenMethod
    def get_by_name_label(self, label: str) -> List['xenbridge.SR']:
        """Get all the SR instances with the given label."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.SR':
        """Get a reference to the SR instance with the specified UUID."""
    @XenMethod
    def get_supported_types(self) -> List[str]:
        """Return a set of all the SR types supported by the system"""
    @XenMethod
    def introduce(self, uuid: str, name_label: str, name_description: str, type: str, content_type: str, shared: bool, sm_config: Dict[str, str]) -> 'xenbridge.SR':
        """Introduce a new Storage Repository into the managed system"""
    @XenMethod
    def make(self, host: 'xenbridge.Host', device_config: Dict[str, str], physical_size: int, name_label: str, name_description: str, type: str, content_type: str, sm_config: Dict[str, str]) -> str:
        """Create a new Storage Repository on disk. This call is deprecated: use SR.create
        instead."""
    @XenMethod
    def probe(self, host: 'xenbridge.Host', device_config: Dict[str, str], type: str, sm_config: Dict[str, str]) -> str:
        """Perform a backend-specific scan, using the given device_config.  If the
        device_config is complete, then this will return a list of the SRs present of
        this type on the device, if any.  If the device_config is partial, then a
        backend-specific scan will be performed, returning results that will guide the
        user in improving the device_config."""
    @XenMethod
    def probe_ext(self, host: 'xenbridge.Host', device_config: Dict[str, str], type: str, sm_config: Dict[str, str]) -> List[Dict[str, Any]]:
        """Perform a backend-specific scan, using the given device_config.  If the
        device_config is complete, then this will return a list of the SRs present of
        this type on the device, if any.  If the device_config is partial, then a
        backend-specific scan will be performed, returning results that will guide the
        user in improving the device_config."""
