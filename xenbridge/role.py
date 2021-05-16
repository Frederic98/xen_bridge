#Automatically generated from https://xapi-project.github.io/xen-api/classes/role.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class Role(XenObject):
    xenpath='role'

    name_description: str = XenProperty(XenProperty.READONLY, 'what this role is for')
    name_label: str = XenProperty(XenProperty.READONLY, 'a short user-friendly name for the role')
    subroles: List['xenbridge.Role'] = XenProperty(XenProperty.READONLY, 'a list of pointers to other roles or permissions')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def get_by_permission(self) -> List['xenbridge.Role']:
        """This call returns a list of roles given a permission"""
    @XenMethod
    def get_permissions(self) -> List['xenbridge.Role']:
        """This call returns a list of permissions given a role"""
    @XenMethod
    def get_permissions_name_label(self) -> List[str]:
        """This call returns a list of permission names given a role"""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given role."""


class RoleEndpoint(XenEndpoint):
    xenpath='role'
    @XenMethod
    def get_all(self) -> List['xenbridge.Role']:
        """Return a list of all the roles known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.Role', Dict[str, Any]]:
        """Return a map of role references to role records for all roles known to the
        system."""
    @XenMethod
    def get_by_name_label(self, label: str) -> List['xenbridge.Role']:
        """Get all the role instances with the given label."""
    @XenMethod
    def get_by_permission_name_label(self, label: str) -> List['xenbridge.Role']:
        """This call returns a list of roles given a permission name"""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.Role':
        """Get a reference to the role instance with the specified UUID."""
