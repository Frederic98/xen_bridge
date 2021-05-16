#Automatically generated from https://xapi-project.github.io/xen-api/classes/vdi_nbd_server_info.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class VdiNbdServerInfo(XenObject):
    xenpath='vdi_nbd_server_info'

    address: str = XenProperty(XenProperty.READONLY, 'An address on which the server can be reached; this can be IPv4, IPv6, or a DNS name.')
    cert: str = XenProperty(XenProperty.READONLY, 'The TLS certificate of the server')
    exportname: str = XenProperty(XenProperty.READONLY, 'The exportname to request over NBD. This holds details including an authentication token, so it must be protected appropriately. Clients should regard the exportname as an opaque string or token.')
    port: int = XenProperty(XenProperty.READONLY, 'The TCP port')
    subject: str = XenProperty(XenProperty.READONLY, 'For convenience, this redundant field holds a DNS (hostname) subject of the certificate. This can be a wildcard, but only for a certificate that has a wildcard subject and no concrete hostname subjects.')


class VdiNbdServerInfoEndpoint(XenEndpoint):
    xenpath='vdi_nbd_server_info'
    ...
