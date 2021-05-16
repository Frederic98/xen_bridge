#Automatically generated from https://xapi-project.github.io/xen-api/classes/data_source.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class DataSource(XenObject):
    xenpath='data_source'

    enabled: bool = XenProperty(XenProperty.READONLY, 'true if the data source is being logged')
    max: float = XenProperty(XenProperty.READONLY, 'the maximum value of the data source')
    min: float = XenProperty(XenProperty.READONLY, 'the minimum value of the data source')
    name_description: str = XenProperty(XenProperty.READONLY, 'a notes field containing human-readable description')
    name_label: str = XenProperty(XenProperty.READONLY, 'a human-readable name')
    standard: bool = XenProperty(XenProperty.READONLY, 'true if the data source is enabled by default. Non-default data sources cannot be disabled')
    units: str = XenProperty(XenProperty.READONLY, 'the units of the value')
    value: float = XenProperty(XenProperty.READONLY, 'current value of the data source')


class DataSourceEndpoint(XenEndpoint):
    xenpath='data_source'
    ...
