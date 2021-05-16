#Automatically generated from https://xapi-project.github.io/xen-api/classes/task.html
import xenbridge
from .xenobject import XenObject, XenEndpoint, XenMethod, XenProperty, XenEnum
from typing import List, Dict, Any, Optional
import datetime


class TaskAllowedOperations(XenEnum):
    CANCEL = 'cancel'
    DESTROY = 'destroy'
class TaskStatusType(XenEnum):
    PENDING = 'pending'
    SUCCESS = 'success'
    FAILURE = 'failure'
    CANCELLING = 'cancelling'
    CANCELLED = 'cancelled'

class Task(XenObject):
    xenpath='task'

    allowed_operations: List[TaskAllowedOperations] = XenProperty(XenProperty.READONLY, 'list of the operations allowed in this state. This list is advisory only and the server state may have changed by the time this field is read by a client.')
    backtrace: str = XenProperty(XenProperty.READONLY, 'Function call trace for debugging.')
    created: datetime.datetime = XenProperty(XenProperty.READONLY, 'Time task was created')
    current_operations: Dict[str, TaskAllowedOperations] = XenProperty(XenProperty.READONLY, 'links each of the running tasks using this object (by reference) to a current_operation enum which describes the nature of the task.')
    error_info: List[str] = XenProperty(XenProperty.READONLY, 'if the task has failed, this field contains the set of associated error strings. Undefined otherwise.')
    finished: datetime.datetime = XenProperty(XenProperty.READONLY, 'Time task finished (i.e. succeeded or failed). If task-status is pending, then the value of this field has no meaning')
    name_description: str = XenProperty(XenProperty.READONLY, 'a notes field containing human-readable description')
    name_label: str = XenProperty(XenProperty.READONLY, 'a human-readable name')
    other_config: Dict[str, str] = XenProperty(XenProperty.READWRITE, 'additional configuration')
    progress: float = XenProperty(XenProperty.READONLY, 'This field contains the estimated fraction of the task which is complete. This field should not be used to determine whether the task is complete - for this the status field of the task should be used.')
    resident_on: 'xenbridge.Host' = XenProperty(XenProperty.READONLY, 'the host on which the task is running')
    result: str = XenProperty(XenProperty.READONLY, 'if the task has completed successfully, this field contains the result value (either Void or an object reference). Undefined otherwise.')
    status: TaskStatusType = XenProperty(XenProperty.READONLY, 'current status of the task')
    subtask_of: 'xenbridge.Task' = XenProperty(XenProperty.READONLY, 'Ref pointing to the task this is a substask of.')
    subtasks: List['xenbridge.Task'] = XenProperty(XenProperty.READONLY, 'List pointing to all the substasks.')
    type: str = XenProperty(XenProperty.READONLY, 'if the task has completed successfully, this field contains the type of the encoded result (i.e. name of the class whose reference is in the result field). Undefined otherwise.')
    uuid: str = XenProperty(XenProperty.READONLY, 'Unique identifier/object reference')

    @XenMethod
    def add_to_other_config(self, key: str, value: str) -> None:
        """Add the given key-value pair to the other_config field of the given task."""
    @XenMethod
    def cancel(self) -> None:
        """Request that a task be cancelled. Note that a task may fail to be cancelled and
        may complete or fail normally and note that, even when a task does cancel, it
        might take an arbitrary amount of time."""
    @XenMethod
    def destroy(self) -> None:
        """Destroy the task object"""
    @XenMethod
    def get_record(self) -> Dict[str, Any]:
        """Get a record containing the current state of the given task."""
    @XenMethod
    def remove_from_other_config(self, key: str) -> None:
        """Remove the given key and its corresponding value from the other_config field of
        the given task.  If the key is not in that Map, then do nothing."""


class TaskEndpoint(XenEndpoint):
    xenpath='task'
    @XenMethod
    def create(self, label: str, description: str) -> 'xenbridge.Task':
        """Create a new task object which must be manually destroyed."""
    @XenMethod
    def get_all(self) -> List['xenbridge.Task']:
        """Return a list of all the tasks known to the system."""
    @XenMethod
    def get_all_records(self) -> Dict['xenbridge.Task', Dict[str, Any]]:
        """Return a map of task references to task records for all tasks known to the
        system."""
    @XenMethod
    def get_by_name_label(self, label: str) -> List['xenbridge.Task']:
        """Get all the task instances with the given label."""
    @XenMethod
    def get_by_uuid(self, uuid: str) -> 'xenbridge.Task':
        """Get a reference to the task instance with the specified UUID."""
