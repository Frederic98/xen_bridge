#Automatically generated from https://xapi-project.github.io/xen-api/classes/certificate.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class Certificate(XenObject):
    xenpath='Certificate'

    fingerprint: str = XenProperty(XenProperty.READONLY, "The certificate's fingerprint / hash")
    host: 'xenbridge.Host' = XenProperty(XenProperty.READONLY, 'The host where the certificate is installed')
    not_after: datetime.datetime = XenProperty(XenProperty.READONLY, 'Date before which the certificate is valid')
    not_before: datetime.datetime = XenProperty(XenProperty.READONLY, 'Date after which the certificate is valid')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given Certificate."""


class CertificateEndpoint(XenEndpoint):
    xenpath='Certificate'
    @XenMethod
    def get_all(self) -> List['xenbridge.Certificate']:
        """Return a list of all the Certificates known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.Certificate', Dict[str, Any]]:
        """Return a map of Certificate references to Certificate records for all
        Certificates known to the system."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.Certificate':
        """Get a reference to the Certificate instance with the specified UUID."""
