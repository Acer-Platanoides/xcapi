# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xcapi/xray/proxy/freedom/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from xcapi.xray.common.protocol.server_spec_pb import ServerEndpoint
from typing import Optional, List
from dataclasses import dataclass
from xcapi.model import ClassMeta
from enum import Enum


@dataclass
class DestinationOverride(ClassMeta):
    server: Optional[ServerEndpoint] = None


@dataclass
class Fragment(ClassMeta):
    packets_from: Optional[int] = None
    packets_to: Optional[int] = None
    length_min: Optional[int] = None
    length_max: Optional[int] = None
    interval_min: Optional[int] = None
    interval_max: Optional[int] = None


@dataclass
class Noise(ClassMeta):
    length_min: Optional[int] = None
    length_max: Optional[int] = None
    delay_min: Optional[int] = None
    delay_max: Optional[int] = None
    str_noise: Optional[bytes] = None


@dataclass
class Config(ClassMeta):
    class DomainStrategy(Enum):
        AS_IS: int = 0
        USE_IP: int = 1
        USE_IP4: int = 2
        USE_IP6: int = 3
        USE_IP46: int = 4
        USE_IP64: int = 5
        FORCE_IP: int = 6
        FORCE_IP4: int = 7
        FORCE_IP6: int = 8
        FORCE_IP46: int = 9
        FORCE_IP64: int = 10

    domain_strategy: Optional[DomainStrategy] = None
    destination_override: Optional[DestinationOverride] = None
    user_level: Optional[int] = None
    fragment: Optional[Fragment] = None
    proxy_protocol: Optional[int] = None
    noises: Optional[List[Noise]] = None


_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n%xcapi/xray/proxy/freedom/config.proto\x12\x12xray.proxy.freedom\x1a,xcapi/xray/common/protocol/server_spec.proto\"K\n\x13\x44\x65stinationOverride\x12\x34\n\x06server\x18\x01 \x01(\x0b\x32$.xray.common.protocol.ServerEndpoint\"\x88\x01\n\x08\x46ragment\x12\x14\n\x0cpackets_from\x18\x01 \x01(\x04\x12\x12\n\npackets_to\x18\x02 \x01(\x04\x12\x12\n\nlength_min\x18\x03 \x01(\x04\x12\x12\n\nlength_max\x18\x04 \x01(\x04\x12\x14\n\x0cinterval_min\x18\x05 \x01(\x04\x12\x14\n\x0cinterval_max\x18\x06 \x01(\x04\"h\n\x05Noise\x12\x12\n\nlength_min\x18\x01 \x01(\x04\x12\x12\n\nlength_max\x18\x02 \x01(\x04\x12\x11\n\tdelay_min\x18\x03 \x01(\x04\x12\x11\n\tdelay_max\x18\x04 \x01(\x04\x12\x11\n\tstr_noise\x18\x05 \x01(\x0c\"\xc6\x03\n\x06\x43onfig\x12\x42\n\x0f\x64omain_strategy\x18\x01 \x01(\x0e\x32).xray.proxy.freedom.Config.DomainStrategy\x12\x45\n\x14\x64\x65stination_override\x18\x03 \x01(\x0b\x32\'.xray.proxy.freedom.DestinationOverride\x12\x12\n\nuser_level\x18\x04 \x01(\r\x12.\n\x08\x66ragment\x18\x05 \x01(\x0b\x32\x1c.xray.proxy.freedom.Fragment\x12\x16\n\x0eproxy_protocol\x18\x06 \x01(\r\x12)\n\x06noises\x18\x07 \x03(\x0b\x32\x19.xray.proxy.freedom.Noise\"\xa9\x01\n\x0e\x44omainStrategy\x12\t\n\x05\x41S_IS\x10\x00\x12\n\n\x06USE_IP\x10\x01\x12\x0b\n\x07USE_IP4\x10\x02\x12\x0b\n\x07USE_IP6\x10\x03\x12\x0c\n\x08USE_IP46\x10\x04\x12\x0c\n\x08USE_IP64\x10\x05\x12\x0c\n\x08\x46ORCE_IP\x10\x06\x12\r\n\tFORCE_IP4\x10\x07\x12\r\n\tFORCE_IP6\x10\x08\x12\x0e\n\nFORCE_IP46\x10\t\x12\x0e\n\nFORCE_IP64\x10\nb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xcapi.xray.proxy.freedom.config_pb', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_DESTINATIONOVERRIDE']._serialized_start = 107
    _globals['_DESTINATIONOVERRIDE']._serialized_end = 182
    _globals['_FRAGMENT']._serialized_start = 185
    _globals['_FRAGMENT']._serialized_end = 321
    _globals['_NOISE']._serialized_start = 323
    _globals['_NOISE']._serialized_end = 427
    _globals['_CONFIG']._serialized_start = 430
    _globals['_CONFIG']._serialized_end = 884
    _globals['_CONFIG_DOMAINSTRATEGY']._serialized_start = 715
    _globals['_CONFIG_DOMAINSTRATEGY']._serialized_end = 884
