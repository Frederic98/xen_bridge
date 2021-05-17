# XEN Bridge
An object-oriented Xen API for python

Tested on XCP-ng, but should also work on XenServer

## Usage
```python
from xenbridge import XenConnection

xen = XenConnection('http://XEN_HOSTNAME', 'root', 'password')

xoa_vm = xen.VM.get_by_uuid('UUID_OF_VM')
# Or by name-label:
# xoa_vm = xen.VM.get_by_name_label('XOA')[0]

print(f'{xoa_vm.name_label} ({xoa_vm.uuid})')
print(f'VM is a template: {xoa_vm.is_a_template}')
xoa_vm.name_description = 'This is a VM'
xoa_vm.start()      # Spin up the VM
```
