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

## How it works
Firstly, `xenboject.py` defines some helper functions and baseclasses for the endpoints that do the actual work of calling the XMLRPC API and casting the data to the corresponding types.  

For each class, there is a file corresponding to that class - for example, `vm.py`. In here, a class that defines the methods and properties can be found. All methods are wrapped using the `@XenMethod` decorator that copies the function's signature and replaces its functionality.
```python
class VM(XenObject):
    @XenMethod
    def start(self, start_paused: bool, force: bool) -> None:
        """Start the specified VM.  This function can only be called with the VM is in the
        Halted State."""
    power_state: VmPowerState = XenProperty(XenProperty.READONLY)
```
As the API responds with a string for numbers, enums and Xen objects, the return type annotations are used to cast the objects to the correct type.

The XenConnection class is the object that is used to interact with the API

## Missing methods
All API methods are generated from the [XenAPI documentation](https://xapi-project.github.io/xen-api/) using `docscraper.py`. If there is a method that is missing, you can either:
- Add it to the corresponding class in the module yourself
- Call it using the class's `call(methodname, *args)` method and manually cast it to the correct data type
