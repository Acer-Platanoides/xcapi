# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xcapi/xray/common/net/port.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from xcapi.model import ClassMeta
from typing import Optional, List
from dataclasses import dataclass


@dataclass
class PortRange(ClassMeta):
    """PortRange represents a range of ports."""
    From: Optional[int] = None
    """The port that this range starts from."""
    To: Optional[int] = None
    """The port that this range ends with (inclusive)."""


@dataclass
class PortList(ClassMeta):
    """PortList is a list of ports."""
    range: Optional[List[PortRange]] = None


_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n xcapi/xray/common/net/port.proto\x12\x0fxray.common.net\"%\n\tPortRange\x12\x0c\n\x04\x46rom\x18\x01 \x01(\r\x12\n\n\x02To\x18\x02 \x01(\r\"5\n\x08PortList\x12)\n\x05range\x18\x01 \x03(\x0b\x32\x1a.xray.common.net.PortRangeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xcapi.xray.common.net.port_pb', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_PORTRANGE']._serialized_start = 53
    _globals['_PORTRANGE']._serialized_end = 90
    _globals['_PORTLIST']._serialized_start = 92
    _globals['_PORTLIST']._serialized_end = 145
