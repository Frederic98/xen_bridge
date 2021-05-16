#Automatically generated from https://xapi-project.github.io/xen-api/classes/subject.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class Subject(XenObject):
    xenpath='subject'

    other_config: Dict[str, str] = XenProperty(XenProperty.READONLY, 'additional configuration')
    roles: List['xenbridge.Role'] = XenProperty(XenProperty.READONLY, 'the roles associated with this subject')
    subject_identifier: str = XenProperty(XenProperty.READONLY, 'the subject identifier, unique in the external directory service')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_roles(self, role: 'xenbridge.Role') -> None:
        """This call adds a new role to a subject"""
    @XenMethod
    def destroy(self) -> None:
        """Destroy the specified subject instance."""
    @XenMethod
    def get_permissions_name_label(self) -> List[str]:
        """This call returns a list of permission names given a subject"""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given subject."""
    @XenMethod
    def remove_from_roles(self, role: 'xenbridge.Role') -> None:
        """This call removes a role from a subject"""


class SubjectEndpoint(XenEndpoint):
    xenpath='subject'
    @XenMethod
    def create(self, args: Dict[str, Any]) -> 'xenbridge.Subject':
        """Create a new subject instance, and return its handle. The constructor args are:
        subject_identifier, other_config (* = non-optional)."""
    @XenMethod
    def get_all(self) -> List['xenbridge.Subject']:
        """Return a list of all the subjects known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.Subject', Dict[str, Any]]:
        """Return a map of subject references to subject records for all subjects known to
        the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.Subject':
        """Get a reference to the subject instance with the specified UUID."""
