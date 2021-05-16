#Automatically generated from https://xapi-project.github.io/xen-api/classes/pif.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class PifIgmpStatus(XenEnum):
    ENABLED = 'enabled'
    DISABLED = 'disabled'
    UNKNOWN = 'unknown'
class IpConfigurationMode(XenEnum):
    NONE = 'None'
    DHCP = 'DHCP'
    STATIC = 'Static'
class Ipv6ConfigurationMode(XenEnum):
    NONE = 'None'
    DHCP = 'DHCP'
    STATIC = 'Static'
    AUTOCONF = 'Autoconf'
class PrimaryAddressType(XenEnum):
    IPV4 = 'IPv4'
    IPV6 = 'IPv6'

class PIF(XenObject):
    xenpath='PIF'

    DNS: str = XenProperty(XenProperty.READONLY, 'Comma separated list of the IP addresses of the DNS servers to use')
    IP: str = XenProperty(XenProperty.READONLY, 'IP address')
    IPv6: List[str] = XenProperty(XenProperty.READONLY, 'IPv6 address')
    MAC: str = XenProperty(XenProperty.READONLY, 'ethernet MAC address of physical interface')
    MTU: int = XenProperty(XenProperty.READONLY, 'MTU in octets')
    PCI: 'xenbridge.PCI' = XenProperty(XenProperty.READONLY, 'Link to underlying PCI device')
    VLAN: int = XenProperty(XenProperty.READONLY, 'VLAN tag for all traffic passing through this interface')
    VLAN_master_of: 'xenbridge.VLAN' = XenProperty(XenProperty.READONLY, 'Indicates wich VLAN this interface receives untagged traffic from')
    VLAN_slave_of: List['xenbridge.VLAN'] = XenProperty(XenProperty.READONLY, 'Indicates which VLANs this interface transmits tagged traffic to')
    bond_master_of: List['xenbridge.Bond'] = XenProperty(XenProperty.READONLY, 'Indicates this PIF represents the results of a bond')
    bond_slave_of: 'xenbridge.Bond' = XenProperty(XenProperty.READONLY, 'Indicates which bond this interface is part of')
    capabilities: List[str] = XenProperty(XenProperty.READONLY, 'Additional capabilities on the interface.')
    currently_attached: bool = XenProperty(XenProperty.READONLY, 'true if this interface is online')
    device: str = XenProperty(XenProperty.READONLY, 'machine-readable name of the interface (e.g. eth0)')
    disallow_unplug: bool = XenProperty(XenProperty.READONLY, "Prevent this PIF from being unplugged; set this to notify the management tool-stack that the PIF has a special use and should not be unplugged under any circumstances (e.g. because you're running storage traffic over it)")
    gateway: str = XenProperty(XenProperty.READONLY, 'IP gateway')
    host: 'xenbridge.Host' = XenProperty(XenProperty.READONLY, 'physical machine to which this pif is connected')
    igmp_snooping_status: PifIgmpStatus = XenProperty(XenProperty.READONLY, 'The IGMP snooping status of the corresponding network bridge')
    ip_configuration_mode: IpConfigurationMode = XenProperty(XenProperty.READONLY, 'Sets if and how this interface gets an IP address')
    ipv6_configuration_mode: Ipv6ConfigurationMode = XenProperty(XenProperty.READONLY, 'Sets if and how this interface gets an IPv6 address')
    ipv6_gateway: str = XenProperty(XenProperty.READONLY, 'IPv6 gateway')
    managed: bool = XenProperty(XenProperty.READONLY, 'Indicates whether the interface is managed by xapi. If it is not, then xapi will not configure the interface, the commands PIF.plug/unplug/reconfigure_ip(v6) cannot be used, nor can the interface be bonded or have VLANs based on top through xapi.')
    management: bool = XenProperty(XenProperty.READONLY, 'Indicates whether the control software is listening for connections on this interface')
    metrics: 'xenbridge.PIFMetrics' = XenProperty(XenProperty.READONLY, 'metrics associated with this PIF')
    netmask: str = XenProperty(XenProperty.READONLY, 'IP netmask')
    network: 'xenbridge.Network' = XenProperty(XenProperty.READONLY, 'virtual network to which this pif is connected')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'Additional configuration')
    physical: bool = XenProperty(XenProperty.READONLY, 'true if this represents a physical network interface')
    primary_address_type: PrimaryAddressType = XenProperty(XenProperty.READONLY, 'Which protocol should define the primary address of this interface')
    properties: Dict[str, str] = XenProperty(XenProperty.READONLY, 'Additional configuration properties for the interface.')
    sriov_logical_PIF_of: List['xenbridge.NetworkSriov'] = XenProperty(XenProperty.READONLY, 'Indicates which network_sriov this interface is logical of')
    sriov_physical_PIF_of: List['xenbridge.NetworkSriov'] = XenProperty(XenProperty.READONLY, 'Indicates which network_sriov this interface is physical of')
    tunnel_access_PIF_of: List['xenbridge.Tunnel'] = XenProperty(XenProperty.READONLY, 'Indicates to which tunnel this PIF gives access')
    tunnel_transport_PIF_of: List['xenbridge.Tunnel'] = XenProperty(XenProperty.READONLY, 'Indicates to which tunnel this PIF provides transport')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given PIF."""
    @XenMethod
    def db_forget(self) -> None:
        """Destroy a PIF database record."""
    @XenMethod
    def destroy(self) -> None:
        """Destroy the PIF object (provided it is a VLAN interface). This call is
        deprecated: use VLAN.destroy or Bond.destroy instead"""
    @XenMethod
    def forget(self) -> None:
        """Destroy the PIF object matching a particular network interface"""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given PIF."""
    @XenMethod
    def plug(self) -> None:
        """Attempt to bring up a physical interface"""
    @XenMethod
    def reconfigure_ip(self, mode: IpConfigurationMode, IP: str, netmask: str, gateway: str, DNS: str) -> None:
        """Reconfigure the IP address settings for this interface"""
    @XenMethod
    def reconfigure_ipv6(self, mode: Ipv6ConfigurationMode, IPv6: str, gateway: str, DNS: str) -> None:
        """Reconfigure the IPv6 address settings for this interface"""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given PIF.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def set_property(self, name: str, value: str) -> None:
        """Set the value of a property of the PIF"""
    @XenMethod
    def unplug(self) -> None:
        """Attempt to bring down a physical interface"""


class PIFEndpoint(XenEndpoint):
    xenpath='PIF'
    @XenMethod
    def create_VLAN(self, device: str, network: 'xenbridge.Network', host: 'xenbridge.Host', VLAN: int) -> 'xenbridge.PIF':
        """Create a VLAN interface from an existing physical interface. This call is
        deprecated: use VLAN.create instead"""
    @XenMethod
    def db_introduce(self, device: str, network: 'xenbridge.Network', host: 'xenbridge.Host', MAC: str, MTU: int, VLAN: int, physical: bool, ip_configuration_mode: IpConfigurationMode, IP: str, netmask: str, gateway: str, DNS: str, bond_slave_of: 'xenbridge.Bond', VLAN_master_of: 'xenbridge.VLAN', management: bool, other_config: Dict[str, str], disallow_unplug: bool, ipv6_configuration_mode: Ipv6ConfigurationMode, IPv6: List[str], ipv6_gateway: str, primary_address_type: PrimaryAddressType, managed: bool, properties: Dict[str, str]) -> 'xenbridge.PIF':
        """Create a new PIF record in the database only"""
    @XenMethod
    def get_all(self) -> List['xenbridge.PIF']:
        """Return a list of all the PIFs known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.PIF', Dict[str, Any]]:
        """Return a map of PIF references to PIF records for all PIFs known to the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.PIF':
        """Get a reference to the PIF instance with the specified UUID."""
    @XenMethod
    def introduce(self, host: 'xenbridge.Host', MAC: str, device: str, managed: bool) -> 'xenbridge.PIF':
        """Create a PIF object matching a particular network interface"""
    @XenMethod
    def scan(self, host: 'xenbridge.Host') -> None:
        """Scan for physical interfaces on a host and create PIF objects to represent them"""
