from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FloodReport(_message.Message):
    __slots__ = ["state"]
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CLEAR: FloodReport.State
    FLOOD: FloodReport.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: FloodReport.State
    def __init__(self, state: _Optional[_Union[FloodReport.State, str]] = ...) -> None: ...
