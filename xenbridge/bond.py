#Automatically generated from https://xapi-project.github.io/xen-api/classes/bond.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class BondMode(XenEnum):
    BALANCE_SLB = 'balance-slb'
    ACTIVE_BACKUP = 'active-backup'
    LACP = 'lacp'

class Bond(XenObject):
    xenpath='Bond'

    auto_update_mac: bool = XenProperty(XenProperty.READONLY, 'true if the MAC was taken from the primary slave when the bond was created, and false if the client specified the MAC')
    links_up: int = XenProperty(XenProperty.READONLY, 'Number of links up in this bond')
    master: 'xenbridge.PIF' = XenProperty(XenProperty.READONLY, 'The bonded interface')
    mode: BondMode = XenProperty(XenProperty.READONLY, 'The algorithm used to distribute traffic among the bonded NICs')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    primary_slave: 'xenbridge.PIF' = XenProperty(XenProperty.READONLY, 'The PIF of which the IP configuration and MAC were copied to the bond, and which will receive all configuration/VLANs/VIFs on the bond if the bond is destroyed')
    properties: Dict[str, str] = XenProperty(XenProperty.READONLY, 'Additional configuration properties specific to the bond mode.')
    slaves: List['xenbridge.PIF'] = XenProperty(XenProperty.READONLY, 'The interfaces which are part of this bond')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given Bond."""
    @XenMethod
    def destroy(self) -> None:
        """Destroy an interface bond"""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given Bond."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given Bond.  If the key is not in that Map, then do nothing."""
    @XenMethod
    def set_property(self, name: str, value: str) -> None:
        """Set the value of a property of the bond"""


class BondEndpoint(XenEndpoint):
    xenpath='Bond'
    @XenMethod
    def create(self, network: 'xenbridge.Network', members: List['xenbridge.PIF'], MAC: str, mode: BondMode, properties: Dict[str, str]) -> 'xenbridge.Bond':
        """Create an interface bond"""
    @XenMethod
    def get_all(self) -> List['xenbridge.Bond']:
        """Return a list of all the Bonds known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.Bond', Dict[str, Any]]:
        """Return a map of Bond references to Bond records for all Bonds known to the
        system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.Bond':
        """Get a reference to the Bond instance with the specified UUID."""
