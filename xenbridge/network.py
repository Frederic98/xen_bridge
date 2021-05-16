#Automatically generated from https://xapi-project.github.io/xen-api/classes/network.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class NetworkOperations(XenEnum):
    ATTACHING = 'attaching'
class NetworkDefaultLockingMode(XenEnum):
    UNLOCKED = 'unlocked'
    DISABLED = 'disabled'
class NetworkPurpose(XenEnum):
    NBD = 'nbd'
    INSECURE_NBD = 'insecure_nbd'

class Network(XenObject):
    xenpath='network'

    MTU: int = XenProperty(XenProperty.READWRITE, 'MTU in octets')
    PIFs: List['xenbridge.PIF'] = XenProperty(XenProperty.READONLY, 'list of connected pifs')
    VIFs: List['xenbridge.VIF'] = XenProperty(XenProperty.READONLY, 'list of connected vifs')
    allowed_operations: List[NetworkOperations] = XenProperty(XenProperty.READONLY, 'list of the operations allowed in this state. This list is advisory only and the server state may have changed by the time this field is read by a client.')
    assigned_ips: Dict['xenbridge.VIF', str] = XenProperty(XenProperty.READONLY, 'The IP addresses assigned to VIFs on networks that have active xapi-managed DHCP')
    blobs: Dict[str, 'xenbridge.Blob'] = XenProperty(XenProperty.READONLY, 'Binary blobs associated with this network')
    bridge: str = XenProperty(XenProperty.READONLY, 'name of the bridge corresponding to this network on the local host')
    current_operations: Dict[str, NetworkOperations] = XenProperty(XenProperty.READONLY, 'links each of the running tasks using this object (by reference) to a current_operation enum which describes the nature of the task.')
    default_locking_mode: NetworkDefaultLockingMode = XenProperty(XenProperty.READONLY, 'The network will use this value to determine the behaviour of all VIFs where locking_mode = default')
    managed: bool = XenProperty(XenProperty.READONLY, 'true if the bridge is managed by xapi')
    name_description: str = XenProperty(XenProperty.READWRITE, 'a notes field containing human-readable description')
    name_label: str = XenProperty(XenProperty.READWRITE, 'a human-readable name')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    purpose: List[NetworkPurpose] = XenProperty(XenProperty.READONLY, 'Set of purposes for which the server will use this network')
    tags: List[str] = XenProperty(XenProperty.READWRITE, 'user-specified tags for categorization purposes')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_purpose(self, value: NetworkPurpose) -> None:
        """Give a network a new purpose (if not present already)"""
    @XenMethod
    def add_tags(self, value: str) -> None:
        """Add the given value to the tags field of the given network.  If the value is
        already in that Set, then do nothing."""
    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given network."""
    @XenMethod
    def create_new_blob(self, name: str, mime_type: str, public: bool) -> 'xenbridge.Blob':
        """Create a placeholder for a named binary blob of data that is associated with
        this pool"""
    @XenMethod
    def destroy(self) -> None:
        """Destroy the specified network instance."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given network."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given network.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_purpose(self, value: NetworkPurpose) -> None:
        """Remove a purpose from a network (if present)"""
    @XenMethod
    def remove_tags(self, value: str) -> None:
        """Remove the given value from the tags field of the given network.  If the value
        is not in that Set, then do nothing."""


class NetworkEndpoint(XenEndpoint):
    xenpath='network'
    @XenMethod
    def create(self, args: Dict[str, Any]) -> 'xenbridge.Network':
        """Create a new network instance, and return its handle. The constructor args are:
        name_label, name_description, MTU, other_config*, bridge, managed, tags (* =
        non-optional)."""
    @XenMethod
    def get_all(self) -> List['xenbridge.Network']:
        """Return a list of all the networks known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.Network', Dict[str, Any]]:
        """Return a map of network references to network records for all networks known to
        the system."""
    @XenMethod
    def get_by_name_label(self, label: str) -> List['xenbridge.Network']:
        """Get all the network instances with the given label."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.Network':
        """Get a reference to the network instance with the specified UUID."""
