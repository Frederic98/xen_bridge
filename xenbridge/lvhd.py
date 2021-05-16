#Automatically generated from https://xapi-project.github.io/xen-api/classes/lvhd.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class LVHD(XenObject):
    xenpath='LVHD'

    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given LVHD."""


class LVHDEndpoint(XenEndpoint):
    xenpath='LVHD'
    @XenMethod
    def enable_thin_provisioning(self, host: 'xenbridge.Host', SR: 'xenbridge.SR', initial_allocation: int, allocation_quantum: int) -> str:
        """Upgrades an LVHD SR to enable thin-provisioning. Future VDIs created in this SR
        will be thinly-provisioned, although existing VDIs will be left alone. Note that
        the SR must be attached to the SRmaster for upgrade to work."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.LVHD':
        """Get a reference to the LVHD instance with the specified UUID."""
