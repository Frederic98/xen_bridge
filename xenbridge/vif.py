#Automatically generated from https://xapi-project.github.io/xen-api/classes/vif.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class VifOperations(XenEnum):
    ATTACH = 'attach'
    PLUG = 'plug'
    UNPLUG = 'unplug'
class VifLockingMode(XenEnum):
    NETWORK_DEFAULT = 'network_default'
    LOCKED = 'locked'
    UNLOCKED = 'unlocked'
    DISABLED = 'disabled'
class VifIpv4ConfigurationMode(XenEnum):
    NONE = 'None'
    STATIC = 'Static'
class VifIpv6ConfigurationMode(XenEnum):
    NONE = 'None'
    STATIC = 'Static'

class VIF(XenObject):
    xenpath='VIF'

    MAC: str = XenProperty(XenProperty.READONLY, 'ethernet MAC address of virtual interface, as exposed to guest')
    MAC_autogenerated: bool = XenProperty(XenProperty.READONLY, 'true if the MAC was autogenerated; false indicates it was set manually')
    MTU: int = XenProperty(XenProperty.READONLY, 'MTU in octets')
    VM: 'xenbridge.VM' = XenProperty(XenProperty.READONLY, 'virtual machine to which this vif is connected')
    allowed_operations: List[VifOperations] = XenProperty(XenProperty.READONLY, 'list of the operations allowed in this state. This list is advisory only and the server state may have changed by the time this field is read by a client.')
    current_operations: Dict[str, VifOperations] = XenProperty(XenProperty.READONLY, 'links each of the running tasks using this object (by reference) to a current_operation enum which describes the nature of the task.')
    currently_attached: bool = XenProperty(XenProperty.READONLY, 'is the device currently attached (erased on reboot)')
    device: str = XenProperty(XenProperty.READONLY, 'order in which VIF backends are created by xapi')
    ipv4_addresses: List[str] = XenProperty(XenProperty.READONLY, 'IPv4 addresses in CIDR format')
    ipv4_allowed: List[str] = XenProperty(XenProperty.READONLY, 'A list of IPv4 addresses which can be used to filter traffic passing through this VIF')
    ipv4_configuration_mode: VifIpv4ConfigurationMode = XenProperty(XenProperty.READONLY, 'Determines whether IPv4 addresses are configured on the VIF')
    ipv4_gateway: str = XenProperty(XenProperty.READONLY, 'IPv4 gateway (the empty string means that no gateway is set)')
    ipv6_addresses: List[str] = XenProperty(XenProperty.READONLY, 'IPv6 addresses in CIDR format')
    ipv6_allowed: List[str] = XenProperty(XenProperty.READONLY, 'A list of IPv6 addresses which can be used to filter traffic passing through this VIF')
    ipv6_configuration_mode: VifIpv6ConfigurationMode = XenProperty(XenProperty.READONLY, 'Determines whether IPv6 addresses are configured on the VIF')
    ipv6_gateway: str = XenProperty(XenProperty.READONLY, 'IPv6 gateway (the empty string means that no gateway is set)')
    locking_mode: VifLockingMode = XenProperty(XenProperty.READONLY, 'current locking mode of the VIF')
    metrics: 'xenbridge.VIFMetrics' = XenProperty(XenProperty.READONLY, 'metrics associated with this VIF')
    network: 'xenbridge.Network' = XenProperty(XenProperty.READONLY, 'virtual network to which this vif is connected')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    qos_algorithm_params: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'parameters for chosen QoS algorithm')
    qos_algorithm_type: str = XenProperty(XenProperty.READWRITE, 'QoS algorithm to use')
    qos_supported_algorithms: List[str] = XenProperty(XenProperty.READONLY, 'supported QoS algorithms for this VIF')
    runtime_properties: Dict[str, str] = XenProperty(XenProperty.READONLY, 'Device runtime properties')
    status_code: int = XenProperty(XenProperty.READONLY, 'error/success code associated with last attach-operation (erased on reboot)')
    status_detail: str = XenProperty(XenProperty.READONLY, 'error/success information associated with last attach-operation status (erased on reboot)')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_ipv4_allowed(self, value: str) -> None:
        """Associates an IPv4 address with this VIF"""
    @XenMethod
    def add_ipv6_allowed(self, value: str) -> None:
        """Associates an IPv6 address with this VIF"""
    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given VIF."""
    @XenMethod
    def add_to_qos_algorithm_params(self, key: str, value: str) -> None:
        """Add the given key-value pair to the qos/algorithm_params field of the given VIF."""
    @XenMethod
    def configure_ipv4(self, mode: VifIpv4ConfigurationMode, address: str, gateway: str) -> None:
        """Configure IPv4 settings for this virtual interface"""
    @XenMethod
    def configure_ipv6(self, mode: VifIpv6ConfigurationMode, address: str, gateway: str) -> None:
        """Configure IPv6 settings for this virtual interface"""
    @XenMethod
    def destroy(self) -> None:
        """Destroy the specified VIF instance."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given VIF."""
    @XenMethod
    def move(self, network: 'xenbridge.Network') -> None:
        """Move the specified VIF to the specified network, even while the VM is running"""
    @XenMethod
    def plug(self) -> None:
        """Hotplug the specified VIF, dynamically attaching it to the running VM"""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given VIF.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_from_qos_algorithm_params(self, key: str) -> None:
        """Remove the given key and its corresponding value from the qos/algorithm_params
        field of the given VIF.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_ipv4_allowed(self, value: str) -> None:
        """Removes an IPv4 address from this VIF"""
    @XenMethod
    def remove_ipv6_allowed(self, value: str) -> None:
        """Removes an IPv6 address from this VIF"""
    @XenMethod
    def unplug(self) -> None:
        """Hot-unplug the specified VIF, dynamically unattaching it from the running VM"""
    @XenMethod
    def unplug_force(self) -> None:
        """Forcibly unplug the specified VIF"""


class VIFEndpoint(XenEndpoint):
    xenpath='VIF'
    @XenMethod
    def create(self, args: Dict[str, Any]) -> 'xenbridge.VIF':
        """Create a new VIF instance, and return its handle. The constructor args are:
        device*, network*, VM*, MAC*, MTU*, other_config*, currently_attached,
        qos_algorithm_type*, qos_algorithm_params*, locking_mode, ipv4_allowed,
        ipv6_allowed (* = non-optional)."""
    @XenMethod
    def get_all(self) -> List['xenbridge.VIF']:
        """Return a list of all the VIFs known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.VIF', Dict[str, Any]]:
        """Return a map of VIF references to VIF records for all VIFs known to the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.VIF':
        """Get a reference to the VIF instance with the specified UUID."""
