# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xcapi/xray/app/dispatcher/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from xcapi.model import ClassMeta
from typing import Optional
from dataclasses import dataclass


@dataclass
class SessionConfig(ClassMeta):
    pass


@dataclass
class Config(ClassMeta):
    settings: Optional[SessionConfig] = None


_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n&xcapi/xray/app/dispatcher/config.proto\x12\x13xray.app.dispatcher\"\x15\n\rSessionConfigJ\x04\x08\x01\x10\x02\">\n\x06\x43onfig\x12\x34\n\x08settings\x18\x01 \x01(\x0b\x32\".xray.app.dispatcher.SessionConfigb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xcapi.xray.app.dispatcher.config_pb', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_SESSIONCONFIG']._serialized_start = 63
    _globals['_SESSIONCONFIG']._serialized_end = 84
    _globals['_CONFIG']._serialized_start = 86
    _globals['_CONFIG']._serialized_end = 148
