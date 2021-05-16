#Automatically generated from https://xapi-project.github.io/xen-api/classes/cluster.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class ClusterOperation(XenEnum):
    ADD = 'add'
    REMOVE = 'remove'
    ENABLE = 'enable'
    DISABLE = 'disable'
    DESTROY = 'destroy'

class Cluster(XenObject):
    xenpath='Cluster'

    allowed_operations: List[ClusterOperation] = XenProperty(XenProperty.READONLY, 'list of the operations allowed in this state. This list is advisory only and the server state may have changed by the time this field is read by a client.')
    cluster_config: Dict[str, str] = XenProperty(XenProperty.READONLY, 'Contains read-only settings for the cluster, such as timeouts and other options. It can only be set at cluster create time')
    cluster_hosts: List['xenbridge.ClusterHost'] = XenProperty(XenProperty.READONLY, 'A list of the cluster_host objects associated with the Cluster')
    cluster_stack: str = XenProperty(XenProperty.READONLY, "Simply the string 'corosync'. No other cluster stacks are currently supported")
    cluster_token: str = XenProperty(XenProperty.READONLY, 'The secret key used by xapi-clusterd when it talks to itself on other hosts')
    current_operations: Dict[str, ClusterOperation] = XenProperty(XenProperty.READONLY, 'links each of the running tasks using this object (by reference) to a current_operation enum which describes the nature of the task.')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'Additional configuration')
    pending_forget: List[str] = XenProperty(XenProperty.READONLY, 'Internal field used by Host.destroy to store the IP of cluster members marked as permanently dead but not yet removed')
    pool_auto_join: bool = XenProperty(XenProperty.READONLY, 'True if automatically joining new pool members to the cluster. This will be `true` in the first release')
    token_timeout: float = XenProperty(XenProperty.READONLY, 'The corosync token timeout in seconds')
    token_timeout_coefficient: float = XenProperty(XenProperty.READONLY, 'The corosync token timeout coefficient in seconds')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given Cluster."""
    @XenMethod
    def destroy(self) -> None:
        """Destroys a Cluster object and the one remaining Cluster_host member"""
    @XenMethod
    def get_network(self) -> 'xenbridge.Network':
        """Returns the network used by the cluster for inter-host communication, i.e. the
        network shared by all cluster host PIFs"""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given Cluster."""
    @XenMethod
    def pool_destroy(self) -> None:
        """Attempt to destroy the Cluster_host objects for all hosts in the pool and then
        destroy the Cluster."""
    @XenMethod
    def pool_force_destroy(self) -> None:
        """Attempt to force destroy the Cluster_host objects, and then destroy the Cluster."""
    @XenMethod
    def pool_resync(self) -> None:
        """Resynchronise the cluster_host objects across the pool. Creates them where they
        need creating and then plugs them"""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given Cluster.  If the key is not in that Map, then do nothing."""


class ClusterEndpoint(XenEndpoint):
    xenpath='Cluster'
    @XenMethod
    def create(self, PIF: 'xenbridge.PIF', cluster_stack: str, pool_auto_join: bool, token_timeout: float, token_timeout_coefficient: float) -> 'xenbridge.Cluster':
        """Creates a Cluster object and one Cluster_host object as its first member"""
    @XenMethod
    def get_all(self) -> List['xenbridge.Cluster']:
        """Return a list of all the Clusters known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.Cluster', Dict[str, Any]]:
        """Return a map of Cluster references to Cluster records for all Clusters known to
        the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.Cluster':
        """Get a reference to the Cluster instance with the specified UUID."""
    @XenMethod
    def pool_create(self, network: 'xenbridge.Network', cluster_stack: str, token_timeout: float, token_timeout_coefficient: float) -> 'xenbridge.Cluster':
        """Attempt to create a Cluster from the entire pool"""
