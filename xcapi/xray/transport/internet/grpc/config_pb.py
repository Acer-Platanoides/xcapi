# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xcapi/xray/transport/internet/grpc/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from typing import Optional
from xcapi.model import ClassMeta
from dataclasses import dataclass


@dataclass
class Config(ClassMeta):
    authority: Optional[str] = None
    service_name: Optional[str] = None
    multi_mode: Optional[bool] = None
    idle_timeout: Optional[int] = None
    health_check_timeout: Optional[int] = None
    permit_without_stream: Optional[bool] = None
    initial_windows_size: Optional[int] = None
    user_agent: Optional[str] = None


_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n/xcapi/xray/transport/internet/grpc/config.proto\x12%xray.transport.internet.grpc.encoding\"\xca\x01\n\x06\x43onfig\x12\x11\n\tauthority\x18\x01 \x01(\t\x12\x14\n\x0cservice_name\x18\x02 \x01(\t\x12\x12\n\nmulti_mode\x18\x03 \x01(\x08\x12\x14\n\x0cidle_timeout\x18\x04 \x01(\x05\x12\x1c\n\x14health_check_timeout\x18\x05 \x01(\x05\x12\x1d\n\x15permit_without_stream\x18\x06 \x01(\x08\x12\x1c\n\x14initial_windows_size\x18\x07 \x01(\x05\x12\x12\n\nuser_agent\x18\x08 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xcapi.xray.transport.internet.grpc.config_pb', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_CONFIG']._serialized_start = 91
    _globals['_CONFIG']._serialized_end = 293
