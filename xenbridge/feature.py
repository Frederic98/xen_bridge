#Automatically generated from https://xapi-project.github.io/xen-api/classes/feature.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class Feature(XenObject):
    xenpath='Feature'

    enabled: bool = XenProperty(XenProperty.READONLY, 'Indicates whether the feature is enabled')
    experimental: bool = XenProperty(XenProperty.READONLY, 'Indicates whether the feature is experimental (as opposed to stable and fully supported)')
    host: 'xenbridge.Host' = XenProperty(XenProperty.READONLY, 'The host where this feature is available')
    name_description: str = XenProperty(XenProperty.READONLY, 'a notes field containing human-readable description')
    name_label: str = XenProperty(XenProperty.READONLY, 'a human-readable name')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')
    version: str = XenProperty(XenProperty.READONLY, 'The version of this feature')

    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given Feature."""


class FeatureEndpoint(XenEndpoint):
    xenpath='Feature'
    @XenMethod
    def get_all(self) -> List['xenbridge.Feature']:
        """Return a list of all the Features known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.Feature', Dict[str, Any]]:
        """Return a map of Feature references to Feature records for all Features known to
        the system."""
    @XenMethod
    def get_by_name_label(self, label: str) -> List['xenbridge.Feature']:
        """Get all the Feature instances with the given label."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.Feature':
        """Get a reference to the Feature instance with the specified UUID."""
