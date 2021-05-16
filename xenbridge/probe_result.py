#Automatically generated from https://xapi-project.github.io/xen-api/classes/probe_result.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class ProbeResult(XenObject):
    xenpath='probe_result'

    complete: bool = XenProperty(XenProperty.READONLY, 'True if this configuration is complete and can be used to call SR.create. False if it requires further iterative calls to SR.probe, to potentially narrow down on a configuration that can be used.')
    configuration: Dict[str, str] = XenProperty(XenProperty.READONLY, 'Plugin-specific configuration which describes where and how to locate the storage repository. This may include the physical block device name, a remote NFS server and path or an RBD storage pool.')
    extra_info: Dict[str, str] = XenProperty(XenProperty.READONLY, 'Additional plugin-specific information about this configuration, that might be of use for an API user. This can for example include the LUN or the WWPN.')
    sr: Optional[Dict[str, Any]] = XenProperty(XenProperty.READONLY, 'Existing SR found for this configuration')


class ProbeResultEndpoint(XenEndpoint):
    xenpath='probe_result'
    ...
