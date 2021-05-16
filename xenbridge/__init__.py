from .pci import PCI, PCIEndpoint
from .vm import VM, VMEndpoint

class XenConnection(XenConnectionBase):
    VM: VMEndpoint
