#Automatically generated from https://xapi-project.github.io/xen-api/classes/vbd.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class VbdOperations(XenEnum):
    ATTACH = 'attach'
    EJECT = 'eject'
    INSERT = 'insert'
    PLUG = 'plug'
    UNPLUG = 'unplug'
    UNPLUG_FORCE = 'unplug_force'
    PAUSE = 'pause'
    UNPAUSE = 'unpause'
class VbdType(XenEnum):
    CD = 'CD'
    DISK = 'Disk'
    FLOPPY = 'Floppy'
class VbdMode(XenEnum):
    RO = 'RO'
    RW = 'RW'

class VBD(XenObject):
    xenpath='VBD'

    VDI: 'xenbridge.VDI' = XenProperty(XenProperty.READONLY, 'the virtual disk')
    VM: 'xenbridge.VM' = XenProperty(XenProperty.READONLY, 'the virtual machine')
    allowed_operations: List[VbdOperations] = XenProperty(XenProperty.READONLY, 'list of the operations allowed in this state. This list is advisory only and the server state may have changed by the time this field is read by a client.')
    bootable: bool = XenProperty(XenProperty.READWRITE, 'true if this VBD is bootable')
    current_operations: Dict[str, VbdOperations] = XenProperty(XenProperty.READONLY, 'links each of the running tasks using this object (by reference) to a current_operation enum which describes the nature of the task.')
    currently_attached: bool = XenProperty(XenProperty.READONLY, 'is the device currently attached (erased on reboot)')
    device: str = XenProperty(XenProperty.READONLY, 'device seen by the guest e.g. hda1')
    empty: bool = XenProperty(XenProperty.READONLY, 'if true this represents an empty drive')
    metrics: 'xenbridge.VBDMetrics' = XenProperty(XenProperty.READONLY, 'metrics associated with this VBD')
    mode: VbdMode = XenProperty(XenProperty.READONLY, 'the mode the VBD should be mounted with')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    qos_algorithm_params: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'parameters for chosen QoS algorithm')
    qos_algorithm_type: str = XenProperty(XenProperty.READWRITE, 'QoS algorithm to use')
    qos_supported_algorithms: List[str] = XenProperty(XenProperty.READONLY, 'supported QoS algorithms for this VBD')
    runtime_properties: Dict[str, str] = XenProperty(XenProperty.READONLY, 'Device runtime properties')
    status_code: int = XenProperty(XenProperty.READONLY, 'error/success code associated with last attach-operation (erased on reboot)')
    status_detail: str = XenProperty(XenProperty.READONLY, 'error/success information associated with last attach-operation status (erased on reboot)')
    storage_lock: bool = XenProperty(XenProperty.READONLY, 'true if a storage level lock was acquired')
    type: VbdType = XenProperty(XenProperty.READWRITE, 'how the VBD will appear to the guest (e.g. disk or CD)')
    unpluggable: bool = XenProperty(XenProperty.READWRITE, 'true if this VBD will support hot-unplug')
    userdevice: str = XenProperty(XenProperty.READWRITE, 'user-friendly device name e.g. 0,1,2,etc.')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given VBD."""
    @XenMethod
    def add_to_qos_algorithm_params(self, key: str, value: str) -> None:
        """Add the given key-value pair to the qos/algorithm_params field of the given VBD."""
    @XenMethod
    def assert_attachable(self) -> None:
        """Throws an error if this VBD could not be attached to this VM if the VM were
        running. Intended for debugging."""
    @XenMethod
    def destroy(self) -> None:
        """Destroy the specified VBD instance."""
    @XenMethod
    def eject(self) -> None:
        """Remove the media from the device and leave it empty"""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given VBD."""
    @XenMethod
    def insert(self, vdi: 'xenbridge.VDI') -> None:
        """Insert new media into the device"""
    @XenMethod
    def plug(self) -> None:
        """Hotplug the specified VBD, dynamically attaching it to the running VM"""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given VBD.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def remove_from_qos_algorithm_params(self, key: str) -> None:
        """Remove the given key and its corresponding value from the qos/algorithm_params
        field of the given VBD.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def unplug(self) -> None:
        """Hot-unplug the specified VBD, dynamically unattaching it from the running VM"""
    @XenMethod
    def unplug_force(self) -> None:
        """Forcibly unplug the specified VBD"""


class VBDEndpoint(XenEndpoint):
    xenpath='VBD'
    @XenMethod
    def create(self, args: Dict[str, Any]) -> 'xenbridge.VBD':
        """Create a new VBD instance, and return its handle. The constructor args are: VM*,
        VDI*, device, userdevice*, bootable*, mode*, type*, unpluggable, empty*,
        other_config*, currently_attached, qos_algorithm_type*, qos_algorithm_params* (*
        = non-optional)."""
    @XenMethod
    def get_all(self) -> List['xenbridge.VBD']:
        """Return a list of all the VBDs known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.VBD', Dict[str, Any]]:
        """Return a map of VBD references to VBD records for all VBDs known to the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.VBD':
        """Get a reference to the VBD instance with the specified UUID."""
