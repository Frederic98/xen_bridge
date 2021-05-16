#Automatically generated from https://xapi-project.github.io/xen-api/classes/vmss.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class VmssFrequency(XenEnum):
    HOURLY = 'hourly'
    DAILY = 'daily'
    WEEKLY = 'weekly'
class VmssType(XenEnum):
    SNAPSHOT = 'snapshot'
    CHECKPOINT = 'checkpoint'
    SNAPSHOT_WITH_QUIESCE = 'snapshot_with_quiesce'

class VMSS(XenObject):
    xenpath='VMSS'

    VMs: List['xenbridge.VM'] = XenProperty(XenProperty.READONLY, 'all VMs attached to this snapshot schedule')
    enabled: bool = XenProperty(XenProperty.READWRITE, 'enable or disable this snapshot schedule')
    frequency: VmssFrequency = XenProperty(XenProperty.READONLY, 'frequency of taking snapshot from snapshot schedule')
    last_run_time: datetime.datetime = XenProperty(XenProperty.READONLY, 'time of the last snapshot')
    name_description: str = XenProperty(XenProperty.READWRITE, 'a notes field containing human-readable description')
    name_label: str = XenProperty(XenProperty.READWRITE, 'a human-readable name')
    retained_snapshots: int = XenProperty(XenProperty.READONLY, 'maximum number of snapshots that should be stored at any time')
    schedule: Dict[str, str] = XenProperty(XenProperty.READONLY, "schedule of the snapshot containing 'hour', 'min', 'days'. Date/time-related information is in Local Timezone")
    type: VmssType = XenProperty(XenProperty.READONLY, 'type of the snapshot schedule')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_schedule(self, key: str, value: str) -> None:
        ...
    @XenMethod
    def destroy(self) -> None:
        """Destroy the specified VMSS instance."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given VMSS."""
    @XenMethod
    def remove_from_schedule(self, key: str) -> None:
        ...
    @XenMethod
    def snapshot_now(self) -> str:
        """This call executes the snapshot schedule immediately"""


class VMSSEndpoint(XenEndpoint):
    xenpath='VMSS'
    @XenMethod
    def create(self, args: Dict[str, Any]) -> 'xenbridge.VMSS':
        """Create a new VMSS instance, and return its handle. The constructor args are:
        name_label, name_description, enabled, type*, retained_snapshots, frequency*,
        schedule (* = non-optional)."""
    @XenMethod
    def get_all(self) -> List['xenbridge.VMSS']:
        """Return a list of all the VMSSs known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.VMSS', Dict[str, Any]]:
        """Return a map of VMSS references to VMSS records for all VMSSs known to the
        system."""
    @XenMethod
    def get_by_name_label(self, label: str) -> List['xenbridge.VMSS']:
        """Get all the VMSS instances with the given label."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.VMSS':
        """Get a reference to the VMSS instance with the specified UUID."""
