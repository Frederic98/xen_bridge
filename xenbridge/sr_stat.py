#Automatically generated from https://xapi-project.github.io/xen-api/classes/sr_stat.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class SrHealth(XenEnum):
    HEALTHY = 'healthy'
    RECOVERING = 'recovering'

class SrStat(XenObject):
    xenpath='sr_stat'

    clustered: bool = XenProperty(XenProperty.READONLY, 'Indicates whether the SR uses clustered local storage.')
    free_space: int = XenProperty(XenProperty.READONLY, 'Number of bytes free on the backing storage (in bytes)')
    health: SrHealth = XenProperty(XenProperty.READONLY, 'The health status of the SR.')
    name_description: str = XenProperty(XenProperty.READONLY, 'Longer, human-readable description of the SR. Descriptions are generally only displayed by clients when the user is examining SRs in detail.')
    name_label: str = XenProperty(XenProperty.READONLY, 'Short, human-readable label for the SR.')
    total_space: int = XenProperty(XenProperty.READONLY, 'Total physical size of the backing storage (in bytes)')
    uuid: Optional[str] = XenProperty(XenProperty.READONLY, 'Uuid that uniquely identifies this SR, if one is available.')


class SrStatEndpoint(XenEndpoint):
    xenpath='sr_stat'
    ...
