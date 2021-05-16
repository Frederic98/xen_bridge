#Automatically generated from https://xapi-project.github.io/xen-api/classes/auth.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class Auth(XenObject):
    xenpath='auth'


class AuthEndpoint(XenEndpoint):
    xenpath='auth'
    @XenMethod
    def get_group_membership(self, subject_identifier: str) -> List[str]:
        """This calls queries the external directory service to obtain the transitively-
        closed set of groups that the the subject_identifier is member of."""
    @XenMethod
    def get_subject_identifier(self, subject_name: str) -> str:
        """This call queries the external directory service to obtain the
        subject_identifier as a string from the human-readable subject_name"""
    @XenMethod
    def get_subject_information_from_identifier(self, subject_identifier: str) -> Dict[str, str]:
        """This call queries the external directory service to obtain the user information
        (e.g. username, organization etc) from the specified subject_identifier"""
