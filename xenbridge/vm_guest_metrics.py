#Automatically generated from https://xapi-project.github.io/xen-api/classes/vm_guest_metrics.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class TristateType(XenEnum):
    YES = 'yes'
    NO = 'no'
    UNSPECIFIED = 'unspecified'

class VMGuestMetrics(XenObject):
    xenpath='VM_guest_metrics'

    PV_drivers_detected: bool = XenProperty(XenProperty.READONLY, "At least one of the guest's devices has successfully connected to the backend.")
    PV_drivers_up_to_date: bool = XenProperty(XenProperty.READONLY, 'Logically equivalent to PV_drivers_detected')
    PV_drivers_version: Dict[str, str] = XenProperty(XenProperty.READONLY, 'version of the PV drivers')
    can_use_hotplug_vbd: TristateType = XenProperty(XenProperty.READONLY, "The guest's statement of whether it supports VBD hotplug, i.e. whether it is capable of responding immediately to instantiation of a new VBD by bringing online a new PV block device. If the guest states that it is not capable, then the VBD plug and unplug operations will not be allowed while the guest is running.")
    can_use_hotplug_vif: TristateType = XenProperty(XenProperty.READONLY, "The guest's statement of whether it supports VIF hotplug, i.e. whether it is capable of responding immediately to instantiation of a new VIF by bringing online a new PV network device. If the guest states that it is not capable, then the VIF plug and unplug operations will not be allowed while the guest is running.")
    disks: Dict[str, str] = XenProperty(XenProperty.READONLY, 'This field exists but has no data.')
    last_updated: datetime.datetime = XenProperty(XenProperty.READONLY, 'Time at which this information was last updated')
    live: bool = XenProperty(XenProperty.READONLY, 'True if the guest is sending heartbeat messages via the guest agent')
    memory: Dict[str, str] = XenProperty(XenProperty.READONLY, 'This field exists but has no data. Use the memory and memory_internal_free RRD data-sources instead.')
    networks: Dict[str, str] = XenProperty(XenProperty.READONLY, 'network configuration')
    os_version: Dict[str, str] = XenProperty(XenProperty.READONLY, 'version of the OS')
    other: Dict[str, str] = XenProperty(XenProperty.READONLY, 'anything else')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given
        VM_guest_metrics."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given VM_guest_metrics."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given VM_guest_metrics.  If the key is not in that Map, then do nothing."""


class VMGuestMetricsEndpoint(XenEndpoint):
    xenpath='VM_guest_metrics'
    @XenMethod
    def get_all(self) -> List['xenbridge.VMGuestMetrics']:
        """Return a list of all the VM_guest_metrics instances known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.VMGuestMetrics', Dict[str, Any]]:
        """Return a map of VM_guest_metrics references to VM_guest_metrics records for all
        VM_guest_metrics instances known to the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.VMGuestMetrics':
        """Get a reference to the VM_guest_metrics instance with the specified UUID."""
