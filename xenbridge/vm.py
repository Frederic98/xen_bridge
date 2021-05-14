from xenbridge.xenobject import XenProperty
from .xenobject import XenEndpoint, XenObject, XenMethod
from typing import List
from .pci import PCI
import xenbridge


class VM(XenObject):
    xenpath = 'VM'

    def __repr__(self) -> str:
        return f"<Xen.VM {'Template ' if self.is_a_template else ''}'{self.get_name_label()}'>"

    @XenMethod
    def get_name_label(self) -> str: ...

    @XenMethod
    def start(self): ...

    @XenMethod
    def shutdown(self): ...

    @XenMethod
    def get_name_label(self) -> str: ...

    is_a_template: bool = XenProperty()

    @XenMethod
    def set_tags(self, tag: str): ...

    @XenMethod
    def set_name_description(self, description: str): ...

    attached_PCIs: List['xenbridge.PCI'] = XenProperty()
    power_state: str = XenProperty(XenProperty.READONLY)


class VMEndpoint(XenEndpoint):
    xenpath = 'VM'

    @XenMethod
    def get_all(self) -> List[VM]: ...

    @XenMethod
    def get_by_uuid(self, uuid: str) -> VM: ...
