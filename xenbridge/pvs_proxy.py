#Automatically generated from https://xapi-project.github.io/xen-api/classes/pvs_proxy.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class PvsProxyStatus(XenEnum):
    STOPPED = 'stopped'
    INITIALISED = 'initialised'
    CACHING = 'caching'
    INCOMPATIBLE_WRITE_CACHE_MODE = 'incompatible_write_cache_mode'
    INCOMPATIBLE_PROTOCOL_VERSION = 'incompatible_protocol_version'

class PVSProxy(XenObject):
    xenpath='PVS_proxy'

    VIF: 'xenbridge.VIF' = XenProperty(XenProperty.READONLY, 'VIF of the VM using the proxy')
    currently_attached: bool = XenProperty(XenProperty.READONLY, 'true = VM is currently proxied')
    site: 'xenbridge.PVSSite' = XenProperty(XenProperty.READONLY, 'PVS site this proxy is part of')
    status: PvsProxyStatus = XenProperty(XenProperty.READONLY, 'The run-time status of the proxy')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def destroy(self) -> None:
        """remove (or switch off) a PVS proxy for this VM"""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given PVS_proxy."""


class PVSProxyEndpoint(XenEndpoint):
    xenpath='PVS_proxy'
    @XenMethod
    def create(self, site: 'xenbridge.PVSSite', VIF: 'xenbridge.VIF') -> 'xenbridge.PVSProxy':
        """Configure a VM/VIF to use a PVS proxy"""
    @XenMethod
    def get_all(self) -> List['xenbridge.PVSProxy']:
        """Return a list of all the PVS_proxys known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.PVSProxy', Dict[str, Any]]:
        """Return a map of PVS_proxy references to PVS_proxy records for all PVS_proxys
        known to the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.PVSProxy':
        """Get a reference to the PVS_proxy instance with the specified UUID."""
