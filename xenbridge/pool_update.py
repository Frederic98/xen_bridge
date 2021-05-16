#Automatically generated from https://xapi-project.github.io/xen-api/classes/pool_update.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class UpdateAfterApplyGuidance(XenEnum):
    RESTARTHVM = 'restartHVM'
    RESTARTPV = 'restartPV'
    RESTARTHOST = 'restartHost'
    RESTARTXAPI = 'restartXAPI'
class LivepatchStatus(XenEnum):
    OK_LIVEPATCH_COMPLETE = 'ok_livepatch_complete'
    OK_LIVEPATCH_INCOMPLETE = 'ok_livepatch_incomplete'
    OK = 'ok'

class PoolUpdate(XenObject):
    xenpath='pool_update'

    after_apply_guidance: List[UpdateAfterApplyGuidance] = XenProperty(XenProperty.READONLY, 'What the client should do after this update has been applied.')
    enforce_homogeneity: bool = XenProperty(XenProperty.READONLY, 'Flag - if true, all hosts in a pool must apply this update')
    hosts: List['xenbridge.Host'] = XenProperty(XenProperty.READONLY, 'The hosts that have applied this update.')
    installation_size: int = XenProperty(XenProperty.READONLY, 'Size of the update in bytes')
    key: str = XenProperty(XenProperty.READONLY, 'GPG key of the update')
    name_description: str = XenProperty(XenProperty.READONLY, 'a notes field containing human-readable description')
    name_label: str = XenProperty(XenProperty.READONLY, 'a human-readable name')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')
    vdi: 'xenbridge.VDI' = XenProperty(XenProperty.READONLY, 'VDI the update was uploaded to')
    version: str = XenProperty(XenProperty.READONLY, 'Update version number')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given pool_update."""
    @XenMethod
    def apply(self, host: 'xenbridge.Host') -> None:
        """Apply the selected update to a host"""
    @XenMethod
    def destroy(self) -> None:
        """Removes the database entry. Only works on unapplied update."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given pool_update."""
    @XenMethod
    def pool_apply(self) -> None:
        """Apply the selected update to all hosts in the pool"""
    @XenMethod
    def pool_clean(self) -> None:
        """Removes the update's files from all hosts in the pool, but does not revert the
        update"""
    @XenMethod
    def precheck(self, host: 'xenbridge.Host') -> LivepatchStatus:
        """Execute the precheck stage of the selected update on a host"""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given pool_update.  If the key is not in that Map, then do nothing."""


class PoolUpdateEndpoint(XenEndpoint):
    xenpath='pool_update'
    @XenMethod
    def get_all(self) -> List['xenbridge.PoolUpdate']:
        """Return a list of all the pool_updates known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.PoolUpdate', Dict[str, Any]]:
        """Return a map of pool_update references to pool_update records for all
        pool_updates known to the system."""
    @XenMethod
    def get_by_name_label(self, label: str) -> List['xenbridge.PoolUpdate']:
        """Get all the pool_update instances with the given label."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.PoolUpdate':
        """Get a reference to the pool_update instance with the specified UUID."""
    @XenMethod
    def introduce(self, vdi: 'xenbridge.VDI') -> 'xenbridge.PoolUpdate':
        """Introduce update VDI"""
