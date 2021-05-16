#Automatically generated from https://xapi-project.github.io/xen-api/classes/vtpm.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class VTPM(XenObject):
    xenpath='VTPM'

    VM: 'xenbridge.VM' = XenProperty(XenProperty.READONLY, 'the virtual machine')
    backend: 'xenbridge.VM' = XenProperty(XenProperty.READONLY, 'the domain where the backend is located')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def destroy(self) -> None:
        """Destroy the specified VTPM instance."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given VTPM."""


class VTPMEndpoint(XenEndpoint):
    xenpath='VTPM'
    @XenMethod
    def create(self, args: Dict[str, Any]) -> 'xenbridge.VTPM':
        """Create a new VTPM instance, and return its handle. The constructor args are:
        VM*, backend* (* = non-optional)."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.VTPM':
        """Get a reference to the VTPM instance with the specified UUID."""
