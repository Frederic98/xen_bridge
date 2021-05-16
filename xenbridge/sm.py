#Automatically generated from https://xapi-project.github.io/xen-api/classes/sm.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class SM(XenObject):
    xenpath='SM'

    capabilities: List[str] = XenProperty(XenProperty.READONLY, 'capabilities of the SM plugin')
    configuration: Dict[str, str] = XenProperty(XenProperty.READONLY, 'names and descriptions of device config keys')
    copyright: str = XenProperty(XenProperty.READONLY, 'Entity which owns the copyright of this plugin')
    driver_filename: str = XenProperty(XenProperty.READONLY, 'filename of the storage driver')
    features: Dict[str, int] = XenProperty(XenProperty.READONLY, 'capabilities of the SM plugin, with capability version numbers')
    name_description: str = XenProperty(XenProperty.READONLY, 'a notes field containing human-readable description')
    name_label: str = XenProperty(XenProperty.READONLY, 'a human-readable name')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    required_api_version: str = XenProperty(XenProperty.READONLY, 'Minimum SM API version required on the server')
    required_cluster_stack: List[str] = XenProperty(XenProperty.READONLY, 'The storage plugin requires that one of these cluster stacks is configured and running.')
    type: str = XenProperty(XenProperty.READONLY, 'SR.type')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')
    vendor: str = XenProperty(XenProperty.READONLY, 'Vendor who created this plugin')
    version: str = XenProperty(XenProperty.READONLY, 'Version of the plugin')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given SM."""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given SM."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given SM.  If the key is not in that Map, then do nothing."""


class SMEndpoint(XenEndpoint):
    xenpath='SM'
    @XenMethod
    def get_all(self) -> List['xenbridge.SM']:
        """Return a list of all the SMs known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.SM', Dict[str, Any]]:
        """Return a map of SM references to SM records for all SMs known to the system."""
    @XenMethod
    def get_by_name_label(self, label: str) -> List['xenbridge.SM']:
        """Get all the SM instances with the given label."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.SM':
        """Get a reference to the SM instance with the specified UUID."""
