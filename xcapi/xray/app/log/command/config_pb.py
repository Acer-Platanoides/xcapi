# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xcapi/xray/app/log/command/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from xcapi.model import ClassMeta
from dataclasses import dataclass


@dataclass
class Config(ClassMeta):
    pass


@dataclass
class RestartLoggerRequest(ClassMeta):
    pass


@dataclass
class RestartLoggerResponse(ClassMeta):
    pass


_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\'xcapi/xray/app/log/command/config.proto\x12\x14xray.app.log.command\"\x08\n\x06\x43onfig\"\x16\n\x14RestartLoggerRequest\"\x17\n\x15RestartLoggerResponse2{\n\rLoggerService\x12j\n\rRestartLogger\x12*.xray.app.log.command.RestartLoggerRequest\x1a+.xray.app.log.command.RestartLoggerResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xcapi.xray.app.log.command.config_pb', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_CONFIG']._serialized_start = 65
    _globals['_CONFIG']._serialized_end = 73
    _globals['_RESTARTLOGGERREQUEST']._serialized_start = 75
    _globals['_RESTARTLOGGERREQUEST']._serialized_end = 97
    _globals['_RESTARTLOGGERRESPONSE']._serialized_start = 99
    _globals['_RESTARTLOGGERRESPONSE']._serialized_end = 122
    _globals['_LOGGERSERVICE']._serialized_start = 124
    _globals['_LOGGERSERVICE']._serialized_end = 247
