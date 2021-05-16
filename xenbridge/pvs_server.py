#Automatically generated from https://xapi-project.github.io/xen-api/classes/pvs_server.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class PVSServer(XenObject):
    xenpath='PVS_server'

    addresses: List[str] = XenProperty(XenProperty.READONLY, 'IPv4 addresses of this server')
    first_port: int = XenProperty(XenProperty.READONLY, 'First UDP port accepted by this server')
    last_port: int = XenProperty(XenProperty.READONLY, 'Last UDP port accepted by this server')
    site: 'xenbridge.PVSSite' = XenProperty(XenProperty.READONLY, 'PVS site this server is part of')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def forget(self) -> None:
        """forget a PVS server"""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given PVS_server."""


class PVSServerEndpoint(XenEndpoint):
    xenpath='PVS_server'
    @XenMethod
    def get_all(self) -> List['xenbridge.PVSServer']:
        """Return a list of all the PVS_servers known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.PVSServer', Dict[str, Any]]:
        """Return a map of PVS_server references to PVS_server records for all PVS_servers
        known to the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.PVSServer':
        """Get a reference to the PVS_server instance with the specified UUID."""
    @XenMethod
    def introduce(self, addresses: List[str], first_port: int, last_port: int, site: 'xenbridge.PVSSite') -> 'xenbridge.PVSServer':
        """introduce new PVS server"""
