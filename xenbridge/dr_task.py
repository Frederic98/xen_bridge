#Automatically generated from https://xapi-project.github.io/xen-api/classes/dr_task.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class DRTask(XenObject):
    xenpath='DR_task'

    introduced_SRs: List['xenbridge.SR'] = XenProperty(XenProperty.READONLY, 'All SRs introduced by this appliance')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def destroy(self) -> None:
        """Destroy the disaster recovery task, detaching and forgetting any SRs introduced
        which are no longer required"""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given DR_task."""


class DRTaskEndpoint(XenEndpoint):
    xenpath='DR_task'
    @XenMethod
    def create(self, type: str, device_config: Dict[str, str], whitelist: List[str]) -> 'xenbridge.DRTask':
        """Create a disaster recovery task which will query the supplied list of devices"""
    @XenMethod
    def get_all(self) -> List['xenbridge.DRTask']:
        """Return a list of all the DR_tasks known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.DRTask', Dict[str, Any]]:
        """Return a map of DR_task references to DR_task records for all DR_tasks known to
        the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.DRTask':
        """Get a reference to the DR_task instance with the specified UUID."""
