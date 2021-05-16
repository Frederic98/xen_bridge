#Automatically generated from https://xapi-project.github.io/xen-api/classes/cluster_host.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class ClusterHostOperation(XenEnum):
    ENABLE = 'enable'
    DISABLE = 'disable'
    DESTROY = 'destroy'

class ClusterHost(XenObject):
    xenpath='Cluster_host'

    PIF: 'xenbridge.PIF' = XenProperty(XenProperty.READONLY, 'Reference to the PIF object')
    allowed_operations: List[ClusterHostOperation] = XenProperty(XenProperty.READONLY, 'list of the operations allowed in this state. This list is advisory only and the server state may have changed by the time this field is read by a client.')
    cluster: 'xenbridge.Cluster' = XenProperty(XenProperty.READONLY, 'Reference to the Cluster object')
    current_operations: Dict[str, ClusterHostOperation] = XenProperty(XenProperty.READONLY, 'links each of the running tasks using this object (by reference) to a current_operation enum which describes the nature of the task.')
    enabled: bool = XenProperty(XenProperty.READONLY, 'Whether the cluster host believes that clustering should be enabled on this host')
    host: 'xenbridge.Host' = XenProperty(XenProperty.READONLY, 'Reference to the Host object')
    joined: bool = XenProperty(XenProperty.READONLY, 'Whether the cluster host has joined the cluster')
    other_config: Dict[str, str] = XenProperty(XenProperty.READONLY, 'Additional configuration')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def destroy(self) -> None:
        """Remove a host from an existing cluster."""
    @XenMethod
    def disable(self) -> None:
        """Disable cluster membership for an enabled cluster host."""
    @XenMethod
    def enable(self) -> None:
        """Enable cluster membership for a disabled cluster host."""
    @XenMethod
    def force_destroy(self) -> None:
        """Remove a host from an existing cluster forcefully."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given Cluster_host."""


class ClusterHostEndpoint(XenEndpoint):
    xenpath='Cluster_host'
    @XenMethod
    def create(self, cluster: 'xenbridge.Cluster', host: 'xenbridge.Host', pif: 'xenbridge.PIF') -> 'xenbridge.ClusterHost':
        """Add a new host to an existing cluster."""
    @XenMethod
    def get_all(self) -> List['xenbridge.ClusterHost']:
        """Return a list of all the Cluster_hosts known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.ClusterHost', Dict[str, Any]]:
        """Return a map of Cluster_host references to Cluster_host records for all
        Cluster_hosts known to the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.ClusterHost':
        """Get a reference to the Cluster_host instance with the specified UUID."""
