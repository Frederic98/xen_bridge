#Automatically generated from https://xapi-project.github.io/xen-api/classes/sdn_controller.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class SdnControllerProtocol(XenEnum):
    SSL = 'ssl'
    PSSL = 'pssl'

class SDNController(XenObject):
    xenpath='SDN_controller'

    address: str = XenProperty(XenProperty.READONLY, 'IP address of the controller')
    port: int = XenProperty(XenProperty.READONLY, 'TCP port of the controller')
    protocol: SdnControllerProtocol = XenProperty(XenProperty.READONLY, 'Protocol to connect with SDN controller')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def forget(self) -> None:
        """Remove the OVS manager of the pool and destroy the db record."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given SDN_controller."""


class SDNControllerEndpoint(XenEndpoint):
    xenpath='SDN_controller'
    @XenMethod
    def get_all(self) -> List['xenbridge.SDNController']:
        """Return a list of all the SDN_controllers known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.SDNController', Dict[str, Any]]:
        """Return a map of SDN_controller references to SDN_controller records for all
        SDN_controllers known to the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.SDNController':
        """Get a reference to the SDN_controller instance with the specified UUID."""
    @XenMethod
    def introduce(self, protocol: SdnControllerProtocol, address: str, port: int) -> 'xenbridge.SDNController':
        """Introduce an SDN controller to the pool."""
