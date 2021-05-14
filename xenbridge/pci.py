from xenbridge.xenobject import XenProperty
from .xenobject import XenEndpoint, XenObject, XenMethod
from typing import List


class PCI(XenObject):
    xenpath = 'PCI'

    def __repr__(self) -> str:
        return f"<Xen.PCI '{self.class_name}'>"

    class_name: str = XenProperty(XenProperty.READONLY)
    dependencies: List['PCI'] = XenProperty(XenProperty.READONLY)
    device_name: str = XenProperty(XenProperty.READONLY)
    driver_name: str = XenProperty(XenProperty.READONLY)
    host: str = XenProperty(XenProperty.READONLY)       # ToDo: change type
    other_config: str = XenProperty()                     # ToDo: change type
    pci_id: str = XenProperty(XenProperty.READONLY)
    record: str = XenProperty(XenProperty.READONLY)     # ToDo: change type
    subsystem_device_name: str = XenProperty(XenProperty.READONLY)
    subsystem_vendor_name: str = XenProperty(XenProperty.READONLY)
    uuid: str = XenProperty(XenProperty.READONLY)
    vendor_name: str = XenProperty(XenProperty.READONLY)

    def remove_from_other_config(self, key: str): ...


class PCIEndpoint(XenEndpoint):
    xenpath = 'PCI'

    @XenMethod
    def get_all(self) -> List[PCI]: ...

    @XenMethod
    def get_by_uuid(self, uuid: str): ...
