#Automatically generated from https://xapi-project.github.io/xen-api/classes/pool_patch.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class AfterApplyGuidance(XenEnum):
    RESTARTHVM = 'restartHVM'
    RESTARTPV = 'restartPV'
    RESTARTHOST = 'restartHost'
    RESTARTXAPI = 'restartXAPI'

class PoolPatch(XenObject):
    xenpath='pool_patch'

    after_apply_guidance: List[AfterApplyGuidance] = XenProperty(XenProperty.READONLY, 'What the client should do after this patch has been applied.')
    host_patches: List['xenbridge.HostPatch'] = XenProperty(XenProperty.READONLY, 'This hosts this patch is applied to.')
    name_description: str = XenProperty(XenProperty.READONLY, 'a notes field containing human-readable description')
    name_label: str = XenProperty(XenProperty.READONLY, 'a human-readable name')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    pool_applied: bool = XenProperty(XenProperty.READONLY, 'This patch should be applied across the entire pool')
    pool_update: 'xenbridge.PoolUpdate' = XenProperty(XenProperty.READONLY, 'A reference to the associated pool_update object')
    size: int = XenProperty(XenProperty.READONLY, 'Size of the patch')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')
    version: str = XenProperty(XenProperty.READONLY, 'Patch version number')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given pool_patch."""
    @XenMethod
    def apply(self, host: 'xenbridge.Host') -> str:
        """Apply the selected patch to a host and return its output"""
    @XenMethod
    def clean(self) -> None:
        """Removes the patch's files from the server"""
    @XenMethod
    def clean_on_host(self, host: 'xenbridge.Host') -> None:
        """Removes the patch's files from the specified host"""
    @XenMethod
    def destroy(self) -> None:
        """Removes the patch's files from all hosts in the pool, and removes the database
        entries.  Only works on unapplied patches."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given pool_patch."""
    @XenMethod
    def pool_apply(self) -> None:
        """Apply the selected patch to all hosts in the pool and return a map of host_ref
        -> patch output"""
    @XenMethod
    def pool_clean(self) -> None:
        """Removes the patch's files from all hosts in the pool, but does not remove the
        database entries"""
    @XenMethod
    def precheck(self, host: 'xenbridge.Host') -> str:
        """Execute the precheck stage of the selected patch on a host and return its output"""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given pool_patch.  If the key is not in that Map, then do nothing."""


class PoolPatchEndpoint(XenEndpoint):
    xenpath='pool_patch'
    @XenMethod
    def get_all(self) -> List['xenbridge.PoolPatch']:
        """Return a list of all the pool_patchs known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.PoolPatch', Dict[str, Any]]:
        """Return a map of pool_patch references to pool_patch records for all pool_patchs
        known to the system."""
    @XenMethod
    def get_by_name_label(self, label: str) -> List['xenbridge.PoolPatch']:
        """Get all the pool_patch instances with the given label."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.PoolPatch':
        """Get a reference to the pool_patch instance with the specified UUID."""
