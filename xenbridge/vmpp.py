#Automatically generated from https://xapi-project.github.io/xen-api/classes/vmpp.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class VmppBackupType(XenEnum):
    SNAPSHOT = 'snapshot'
    CHECKPOINT = 'checkpoint'
class VmppBackupFrequency(XenEnum):
    HOURLY = 'hourly'
    DAILY = 'daily'
    WEEKLY = 'weekly'
class VmppArchiveFrequency(XenEnum):
    NEVER = 'never'
    ALWAYS_AFTER_BACKUP = 'always_after_backup'
    DAILY = 'daily'
    WEEKLY = 'weekly'
class VmppArchiveTargetType(XenEnum):
    NONE = 'none'
    CIFS = 'cifs'
    NFS = 'nfs'

class VMPP(XenObject):
    xenpath='VMPP'

    VMs: List['xenbridge.VM'] = XenProperty(XenProperty.READONLY, 'all VMs attached to this protection policy')
    alarm_config: Dict[str, str] = XenProperty(XenProperty.READONLY, 'configuration for the alarm')
    archive_frequency: VmppArchiveFrequency = XenProperty(XenProperty.READONLY, 'frequency of the archive schedule')
    archive_last_run_time: datetime.datetime = XenProperty(XenProperty.READONLY, 'time of the last archive')
    archive_schedule: Dict[str, str] = XenProperty(XenProperty.READONLY, "schedule of the archive containing 'hour', 'min', 'days'. Date/time-related information is in Local Timezone")
    archive_target_config: Dict[str, str] = XenProperty(XenProperty.READONLY, "configuration for the archive, including its 'location', 'username', 'password'")
    archive_target_type: VmppArchiveTargetType = XenProperty(XenProperty.READONLY, 'type of the archive target config')
    backup_frequency: VmppBackupFrequency = XenProperty(XenProperty.READONLY, 'frequency of the backup schedule')
    backup_last_run_time: datetime.datetime = XenProperty(XenProperty.READONLY, 'time of the last backup')
    backup_retention_value: int = XenProperty(XenProperty.READONLY, 'maximum number of backups that should be stored at any time')
    backup_schedule: Dict[str, str] = XenProperty(XenProperty.READONLY, "schedule of the backup containing 'hour', 'min', 'days'. Date/time-related information is in Local Timezone")
    backup_type: VmppBackupType = XenProperty(XenProperty.READWRITE, 'type of the backup sub-policy')
    is_alarm_enabled: bool = XenProperty(XenProperty.READONLY, 'true if alarm is enabled for this policy')
    is_archive_running: bool = XenProperty(XenProperty.READONLY, "true if this protection policy's archive is running")
    is_backup_running: bool = XenProperty(XenProperty.READONLY, "true if this protection policy's backup is running")
    is_policy_enabled: bool = XenProperty(XenProperty.READWRITE, 'enable or disable this policy')
    name_description: str = XenProperty(XenProperty.READWRITE, 'a notes field containing human-readable description')
    name_label: str = XenProperty(XenProperty.READWRITE, 'a human-readable name')
    recent_alerts: List[str] = XenProperty(XenProperty.READONLY, 'recent alerts')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_alarm_config(self, key: str, value: str) -> None:
        ...
    @XenMethod
    def add_to_archive_schedule(self, key: str, value: str) -> None:
        ...
    @XenMethod
    def add_to_archive_target_config(self, key: str, value: str) -> None:
        ...
    @XenMethod
    def add_to_backup_schedule(self, key: str, value: str) -> None:
        ...
    @XenMethod
    def destroy(self) -> None:
        """Destroy the specified VMPP instance."""
    @XenMethod
    def get_alerts(self, hours_from_now: int) -> List[str]:
        """This call fetches a history of alerts for a given protection policy"""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given VMPP."""
    @XenMethod
    def protect_now(self) -> str:
        """This call executes the protection policy immediately"""
    @XenMethod
    def remove_from_alarm_config(self, key: str) -> None:
        ...
    @XenMethod
    def remove_from_archive_schedule(self, key: str) -> None:
        ...
    @XenMethod
    def remove_from_archive_target_config(self, key: str) -> None:
        ...
    @XenMethod
    def remove_from_backup_schedule(self, key: str) -> None:
        ...


class VMPPEndpoint(XenEndpoint):
    xenpath='VMPP'
    @XenMethod
    def archive_now(self, snapshot: 'xenbridge.VM') -> str:
        """This call archives the snapshot provided as a parameter"""
    @XenMethod
    def create(self, args: Dict[str, Any]) -> 'xenbridge.VMPP':
        """Create a new VMPP instance, and return its handle. The constructor args are:
        name_label, name_description, is_policy_enabled, backup_type,
        backup_retention_value, backup_frequency, backup_schedule, archive_target_type,
        archive_target_config, archive_frequency, archive_schedule, is_alarm_enabled,
        alarm_config (* = non-optional)."""
    @XenMethod
    def get_all(self) -> List['xenbridge.VMPP']:
        """Return a list of all the VMPPs known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.VMPP', Dict[str, Any]]:
        """Return a map of VMPP references to VMPP records for all VMPPs known to the
        system."""
    @XenMethod
    def get_by_name_label(self, label: str) -> List['xenbridge.VMPP']:
        """Get all the VMPP instances with the given label."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.VMPP':
        """Get a reference to the VMPP instance with the specified UUID."""
