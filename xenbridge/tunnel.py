#Automatically generated from https://xapi-project.github.io/xen-api/classes/tunnel.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class TunnelProtocol(XenEnum):
    GRE = 'gre'
    VXLAN = 'vxlan'

class Tunnel(XenObject):
    xenpath='tunnel'

    access_PIF: 'xenbridge.PIF' = XenProperty(XenProperty.READONLY, 'The interface through which the tunnel is accessed')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'Additional configuration')
    protocol: TunnelProtocol = XenProperty(XenProperty.READWRITE, 'The protocol used for tunneling (either GRE or VxLAN)')
    status: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'Status information about the tunnel')
    transport_PIF: 'xenbridge.PIF' = XenProperty(XenProperty.READONLY, 'The interface used by the tunnel')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given tunnel."""
    @XenMethod
    def add_to_status(self, key: str, value: str) -> None:
        """Add the given key-value pair to the status field of the given tunnel."""
    @XenMethod
    def destroy(self) -> None:
        """Destroy a tunnel"""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given tunnel."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given tunnel.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_from_status(self, key: str) -> None:
        """Remove the given key and its corresponding value from the status field of the
        given tunnel.  If the key is not in that Map, then do nothing."""


class TunnelEndpoint(XenEndpoint):
    xenpath='tunnel'
    @XenMethod
    def create(self, transport_PIF: 'xenbridge.PIF', network: 'xenbridge.Network', protocol: TunnelProtocol) -> 'xenbridge.Tunnel':
        """Create a tunnel"""
    @XenMethod
    def get_all(self) -> List['xenbridge.Tunnel']:
        """Return a list of all the tunnels known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.Tunnel', Dict[str, Any]]:
        """Return a map of tunnel references to tunnel records for all tunnels known to the
        system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.Tunnel':
        """Get a reference to the tunnel instance with the specified UUID."""
