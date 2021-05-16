#Automatically generated from https://xapi-project.github.io/xen-api/classes/pvs_site.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class PVSSite(XenObject):
    xenpath='PVS_site'

    PVS_uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier of the PVS site, as configured in PVS')
    cache_storage: List['xenbridge.PVSCacheStorage'] = XenProperty(XenProperty.READONLY, 'The SR used by PVS proxy for the cache')
    name_description: str = XenProperty(XenProperty.READWRITE, 'a notes field containing human-readable description')
    name_label: str = XenProperty(XenProperty.READWRITE, 'a human-readable name')
    proxies: List['xenbridge.PVSProxy'] = XenProperty(XenProperty.READONLY, 'The set of proxies associated with the site')
    servers: List['xenbridge.PVSServer'] = XenProperty(XenProperty.READONLY, 'The set of PVS servers in the site')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def forget(self) -> None:
        """Remove a site's meta data"""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given PVS_site."""


class PVSSiteEndpoint(XenEndpoint):
    xenpath='PVS_site'
    @XenMethod
    def get_all(self) -> List['xenbridge.PVSSite']:
        """Return a list of all the PVS_sites known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.PVSSite', Dict[str, Any]]:
        """Return a map of PVS_site references to PVS_site records for all PVS_sites known
        to the system."""
    @XenMethod
    def get_by_name_label(self, label: str) -> List['xenbridge.PVSSite']:
        """Get all the PVS_site instances with the given label."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.PVSSite':
        """Get a reference to the PVS_site instance with the specified UUID."""
    @XenMethod
    def introduce(self, name_label: str, name_description: str, PVS_uuid: str) -> 'xenbridge.PVSSite':
        """Introduce new PVS site"""
