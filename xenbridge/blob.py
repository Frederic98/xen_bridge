#Automatically generated from https://xapi-project.github.io/xen-api/classes/blob.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class Blob(XenObject):
    xenpath='blob'

    last_updated: datetime.datetime = XenProperty(XenProperty.READONLY, 'Time at which the data in the blob was last updated')
    mime_type: str = XenProperty(XenProperty.READONLY, "The mime type associated with this object. Defaults to 'application/octet-stream' if the empty string is supplied")
    name_description: str = XenProperty(XenProperty.READWRITE, 'a notes field containing human-readable description')
    name_label: str = XenProperty(XenProperty.READWRITE, 'a human-readable name')
    public: bool = XenProperty(XenProperty.READWRITE, 'True if the blob is publicly accessible')
    size: int = XenProperty(XenProperty.READONLY, 'Size of the binary data, in bytes')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def destroy(self) -> None:
        ...
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given blob."""


class BlobEndpoint(XenEndpoint):
    xenpath='blob'
    @XenMethod
    def create(self, mime_type: str, public: bool) -> 'xenbridge.Blob':
        """Create a placeholder for a binary blob"""
    @XenMethod
    def get_all(self) -> List['xenbridge.Blob']:
        """Return a list of all the blobs known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.Blob', Dict[str, Any]]:
        """Return a map of blob references to blob records for all blobs known to the
        system."""
    @XenMethod
    def get_by_name_label(self, label: str) -> List['xenbridge.Blob']:
        """Get all the blob instances with the given label."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.Blob':
        """Get a reference to the blob instance with the specified UUID."""
