# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xcapi/xray/app/commander/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from xcapi.model import ClassMeta
from typing import Optional, List
from dataclasses import dataclass
from xcapi.xray.common.serial.typed_message_pb import TypedMessage


@dataclass
class Config(ClassMeta):
    """Config is the settings for Commander."""
    tag: Optional[str] = None
    """Tag of the outbound handler that handles grpc connections."""
    listen: Optional[str] = None
    """Network address of commander grpc service."""
    service: Optional[List[TypedMessage]] = None
    """Services that supported by this server. All services must implement Service interface"""


class ReflectionConfig(ClassMeta):
    """ReflectionConfig is the placeholder config for ReflectionService."""
    pass


_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n%xcapi/xray/app/commander/config.proto\x12\x12xray.app.commander\x1a,xcapi/xray/common/serial/typed_message.proto\"X\n\x06\x43onfig\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x0e\n\x06listen\x18\x03 \x01(\t\x12\x31\n\x07service\x18\x02 \x03(\x0b\x32 .xray.common.serial.TypedMessage\"\x12\n\x10ReflectionConfigb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xcapi.xray.app.commander.config_pb', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_CONFIG']._serialized_start = 107
    _globals['_CONFIG']._serialized_end = 195
    _globals['_REFLECTIONCONFIG']._serialized_start = 197
    _globals['_REFLECTIONCONFIG']._serialized_end = 215
