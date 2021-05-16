#Automatically generated from https://xapi-project.github.io/xen-api/classes/pvs_cache_storage.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class PVSCacheStorage(XenObject):
    xenpath='PVS_cache_storage'

    SR: 'xenbridge.SR' = XenProperty(XenProperty.READONLY, 'SR providing storage for the PVS cache')
    VDI: 'xenbridge.VDI' = XenProperty(XenProperty.READONLY, 'The VDI used for caching')
    host: 'xenbridge.Host' = XenProperty(XenProperty.READONLY, 'The host on which this object defines PVS cache storage')
    site: 'xenbridge.PVSSite' = XenProperty(XenProperty.READONLY, 'The PVS_site for which this object defines the storage')
    size: int = XenProperty(XenProperty.READONLY, 'The size of the cache VDI (in bytes)')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def destroy(self) -> None:
        """Destroy the specified PVS_cache_storage instance."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given PVS_cache_storage."""


class PVSCacheStorageEndpoint(XenEndpoint):
    xenpath='PVS_cache_storage'
    @XenMethod
    def create(self, args: Dict[str, Any]) -> 'xenbridge.PVSCacheStorage':
        """Create a new PVS_cache_storage instance, and return its handle. The constructor
        args are: host, SR, site, size (* = non-optional)."""
    @XenMethod
    def get_all(self) -> List['xenbridge.PVSCacheStorage']:
        """Return a list of all the PVS_cache_storages known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.PVSCacheStorage', Dict[str, Any]]:
        """Return a map of PVS_cache_storage references to PVS_cache_storage records for
        all PVS_cache_storages known to the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.PVSCacheStorage':
        """Get a reference to the PVS_cache_storage instance with the specified UUID."""
