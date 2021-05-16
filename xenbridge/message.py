#Automatically generated from https://xapi-project.github.io/xen-api/classes/message.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class Cls(XenEnum):
    VM = 'VM'
    HOST = 'Host'
    SR = 'SR'
    POOL = 'Pool'
    VMPP = 'VMPP'
    VMSS = 'VMSS'
    PVS_PROXY = 'PVS_proxy'
    VDI = 'VDI'

class Message(XenObject):
    xenpath='message'

    body: str = XenProperty(XenProperty.READONLY, 'The body of the message')
    cls: Cls = XenProperty(XenProperty.READONLY, 'The class of the object this message is associated with')
    name: str = XenProperty(XenProperty.READONLY, 'The name of the message')
    obj_uuid: str = XenProperty(XenProperty.READONLY, 'The uuid of the object this message is associated with')
    priority: int = XenProperty(XenProperty.READONLY, 'The message priority, 0 being low priority')
    timestamp: datetime.datetime = XenProperty(XenProperty.READONLY, 'The time at which the message was created')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def destroy(self) -> None:
        ...
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        ...


class MessageEndpoint(XenEndpoint):
    xenpath='message'
    @XenMethod
    def create(self, name: str, priority: int, cls: Cls, obj_uuid: str, body: str) -> 'xenbridge.Message':
        ...
    @XenMethod
    def get(self, cls: Cls, obj_uuid: str, since: datetime.datetime) -> Dict['xenbridge.Message', Dict[str, Any]]:
        ...
    @XenMethod
    def get_all(self) -> List['xenbridge.Message']:
        ...
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.Message', Dict[str, Any]]:
        ...
    @XenMethod
    def get_all_records_where(self, expr: str) -> Dict['xenbridge.Message', Dict[str, Any]]:
        ...
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.Message':
        ...
    @XenMethod
    def get_since(self, since: datetime.datetime) -> Dict['xenbridge.Message', Dict[str, Any]]:
        ...
