# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xcapi/xray/transport/internet/splithttp/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from typing import Optional, Dict
from xcapi.model import ClassMeta
from dataclasses import dataclass
from xcapi.xray.transport.internet.config_pb import StreamConfig


@dataclass
class RandRangeConfig(ClassMeta):
    to: Optional[int] = None

    def setFrom(self, value: int) -> 'RandRangeConfig':
        self.__setattr__('from', value)
        return self


@dataclass
class Multiplexing(ClassMeta):
    maxConcurrency: Optional[RandRangeConfig] = None
    maxConnections: Optional[RandRangeConfig] = None
    cMaxReuseTimes: Optional[RandRangeConfig] = None
    cMaxLifetimeMs: Optional[RandRangeConfig] = None


@dataclass
class Config(ClassMeta):
    host: Optional[str] = None
    path: Optional[str] = None
    header: Optional[Dict[str, str]] = None
    scMaxConcurrentPosts: Optional[RandRangeConfig] = None
    scMaxEachPostBytes: Optional[RandRangeConfig] = None
    scMinPostsIntervalMs: Optional[RandRangeConfig] = None
    noSSEHeader: Optional[bool] = None
    xPaddingBytes: Optional[RandRangeConfig] = None
    xmux: Optional[Multiplexing] = None
    downloadSettings: Optional[StreamConfig] = None
    mode: Optional[str] = None
    noGRPCHeader: Optional[bool] = None
    keepAlivePeriod: Optional[int] = None


_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n4xcapi/xray/transport/internet/splithttp/config.proto\x12!xray.transport.internet.splithttp\x1a*xcapi/xray/transport/internet/config.proto\"\xab\x05\n\x06\x43onfig\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x45\n\x06header\x18\x03 \x03(\x0b\x32\x35.xray.transport.internet.splithttp.Config.HeaderEntry\x12P\n\x14scMaxConcurrentPosts\x18\x04 \x01(\x0b\x32\x32.xray.transport.internet.splithttp.RandRangeConfig\x12N\n\x12scMaxEachPostBytes\x18\x05 \x01(\x0b\x32\x32.xray.transport.internet.splithttp.RandRangeConfig\x12P\n\x14scMinPostsIntervalMs\x18\x06 \x01(\x0b\x32\x32.xray.transport.internet.splithttp.RandRangeConfig\x12\x13\n\x0bnoSSEHeader\x18\x07 \x01(\x08\x12I\n\rxPaddingBytes\x18\x08 \x01(\x0b\x32\x32.xray.transport.internet.splithttp.RandRangeConfig\x12=\n\x04xmux\x18\t \x01(\x0b\x32/.xray.transport.internet.splithttp.Multiplexing\x12?\n\x10\x64ownloadSettings\x18\n \x01(\x0b\x32%.xray.transport.internet.StreamConfig\x12\x0c\n\x04mode\x18\x0b \x01(\t\x12\x14\n\x0cnoGRPCHeader\x18\x0c \x01(\x08\x12\x17\n\x0fkeepAlivePeriod\x18\r \x01(\x03\x1a-\n\x0bHeaderEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"+\n\x0fRandRangeConfig\x12\x0c\n\x04\x66rom\x18\x01 \x01(\x05\x12\n\n\x02to\x18\x02 \x01(\x05\"\xbe\x02\n\x0cMultiplexing\x12J\n\x0emaxConcurrency\x18\x01 \x01(\x0b\x32\x32.xray.transport.internet.splithttp.RandRangeConfig\x12J\n\x0emaxConnections\x18\x02 \x01(\x0b\x32\x32.xray.transport.internet.splithttp.RandRangeConfig\x12J\n\x0e\x63MaxReuseTimes\x18\x03 \x01(\x0b\x32\x32.xray.transport.internet.splithttp.RandRangeConfig\x12J\n\x0e\x63MaxLifetimeMs\x18\x04 \x01(\x0b\x32\x32.xray.transport.internet.splithttp.RandRangeConfigb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xcapi.xray.transport.internet.splithttp.config_pb', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_CONFIG_HEADERENTRY']._loaded_options = None
    _globals['_CONFIG_HEADERENTRY']._serialized_options = b'8\001'
    _globals['_CONFIG']._serialized_start = 136
    _globals['_CONFIG']._serialized_end = 819
    _globals['_CONFIG_HEADERENTRY']._serialized_start = 774
    _globals['_CONFIG_HEADERENTRY']._serialized_end = 819
    _globals['_RANDRANGECONFIG']._serialized_start = 821
    _globals['_RANDRANGECONFIG']._serialized_end = 864
    _globals['_MULTIPLEXING']._serialized_start = 867
    _globals['_MULTIPLEXING']._serialized_end = 1185
