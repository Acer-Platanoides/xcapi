# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xcapi/xray/proxy/vmess/inbound/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from typing import Optional, List
from dataclasses import dataclass
from xcapi.model import ClassMeta
from xcapi.xray.common.protocol.user_pb import User


@dataclass
class DetourConfig(ClassMeta):
    to: Optional[str] = None


@dataclass
class DefaultConfig(ClassMeta):
    level: Optional[int] = None


@dataclass
class Config(ClassMeta):
    user: Optional[List[User]] = None
    default: Optional[DefaultConfig] = None
    detour: Optional[DetourConfig] = None


_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n+xcapi/xray/proxy/vmess/inbound/config.proto\x12\x18xray.proxy.vmess.inbound\x1a%xcapi/xray/common/protocol/user.proto\"\x1a\n\x0c\x44\x65tourConfig\x12\n\n\x02to\x18\x01 \x01(\t\"\x1e\n\rDefaultConfig\x12\r\n\x05level\x18\x02 \x01(\r\"\xa4\x01\n\x06\x43onfig\x12(\n\x04user\x18\x01 \x03(\x0b\x32\x1a.xray.common.protocol.User\x12\x38\n\x07\x64\x65\x66\x61ult\x18\x02 \x01(\x0b\x32\'.xray.proxy.vmess.inbound.DefaultConfig\x12\x36\n\x06\x64\x65tour\x18\x03 \x01(\x0b\x32&.xray.proxy.vmess.inbound.DetourConfigb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xcapi.xray.proxy.vmess.inbound.config_pb', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_DETOURCONFIG']._serialized_start = 112
    _globals['_DETOURCONFIG']._serialized_end = 138
    _globals['_DEFAULTCONFIG']._serialized_start = 140
    _globals['_DEFAULTCONFIG']._serialized_end = 170
    _globals['_CONFIG']._serialized_start = 173
    _globals['_CONFIG']._serialized_end = 337
