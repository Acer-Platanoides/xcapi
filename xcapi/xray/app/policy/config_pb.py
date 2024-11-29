# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xcapi/xray/app/policy/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from typing import Optional, Dict
from xcapi.model import ClassMeta
from dataclasses import dataclass


@dataclass
class Second(ClassMeta):
    value: Optional[int] = None


@dataclass
class Policy(ClassMeta):
    @dataclass
    class Timeout(ClassMeta):
        """Timeout is a message for timeout settings in various stages, in seconds."""
        handshake: Optional[Second] = None
        connection_idle: Optional[Second] = None
        uplink_only: Optional[Second] = None
        downlink_only: Optional[Second] = None

    @dataclass
    class Stats(ClassMeta):
        user_uplink: Optional[bool] = None
        user_downlink: Optional[bool] = None
        user_online: Optional[bool] = None

    @dataclass
    class Buffer(ClassMeta):
        connection: Optional[int] = None
        """Buffer size per connection, in bytes. -1 for unlimited buffer."""

    timeout: Optional[Timeout] = None
    stats: Optional[Stats] = None
    buffer: Optional[Buffer] = None


@dataclass
class SystemPolicy(ClassMeta):
    @dataclass
    class Stats(ClassMeta):
        inbound_uplink: Optional[bool] = None
        inbound_downlink: Optional[bool] = None
        outbound_uplink: Optional[bool] = None
        outbound_downlink: Optional[bool] = None

    stats: Optional[Stats] = None


@dataclass
class Config(ClassMeta):
    level: Optional[Dict[int, Policy]] = None
    system: Optional[SystemPolicy] = None


_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\"xcapi/xray/app/policy/config.proto\x12\x0fxray.app.policy\"\x17\n\x06Second\x12\r\n\x05value\x18\x01 \x01(\r\"\xc8\x03\n\x06Policy\x12\x30\n\x07timeout\x18\x01 \x01(\x0b\x32\x1f.xray.app.policy.Policy.Timeout\x12,\n\x05stats\x18\x02 \x01(\x0b\x32\x1d.xray.app.policy.Policy.Stats\x12.\n\x06\x62uffer\x18\x03 \x01(\x0b\x32\x1e.xray.app.policy.Policy.Buffer\x1a\xc5\x01\n\x07Timeout\x12*\n\thandshake\x18\x01 \x01(\x0b\x32\x17.xray.app.policy.Second\x12\x30\n\x0f\x63onnection_idle\x18\x02 \x01(\x0b\x32\x17.xray.app.policy.Second\x12,\n\x0buplink_only\x18\x03 \x01(\x0b\x32\x17.xray.app.policy.Second\x12.\n\rdownlink_only\x18\x04 \x01(\x0b\x32\x17.xray.app.policy.Second\x1aH\n\x05Stats\x12\x13\n\x0buser_uplink\x18\x01 \x01(\x08\x12\x15\n\ruser_downlink\x18\x02 \x01(\x08\x12\x13\n\x0buser_online\x18\x03 \x01(\x08\x1a\x1c\n\x06\x42uffer\x12\x12\n\nconnection\x18\x01 \x01(\x05\"\xb1\x01\n\x0cSystemPolicy\x12\x32\n\x05stats\x18\x01 \x01(\x0b\x32#.xray.app.policy.SystemPolicy.Stats\x1am\n\x05Stats\x12\x16\n\x0einbound_uplink\x18\x01 \x01(\x08\x12\x18\n\x10inbound_downlink\x18\x02 \x01(\x08\x12\x17\n\x0foutbound_uplink\x18\x03 \x01(\x08\x12\x19\n\x11outbound_downlink\x18\x04 \x01(\x08\"\xb1\x01\n\x06\x43onfig\x12\x31\n\x05level\x18\x01 \x03(\x0b\x32\".xray.app.policy.Config.LevelEntry\x12-\n\x06system\x18\x02 \x01(\x0b\x32\x1d.xray.app.policy.SystemPolicy\x1a\x45\n\nLevelEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.xray.app.policy.Policy:\x02\x38\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xcapi.xray.app.policy.config_pb', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_CONFIG_LEVELENTRY']._loaded_options = None
    _globals['_CONFIG_LEVELENTRY']._serialized_options = b'8\001'
    _globals['_SECOND']._serialized_start = 55
    _globals['_SECOND']._serialized_end = 78
    _globals['_POLICY']._serialized_start = 81
    _globals['_POLICY']._serialized_end = 537
    _globals['_POLICY_TIMEOUT']._serialized_start = 236
    _globals['_POLICY_TIMEOUT']._serialized_end = 433
    _globals['_POLICY_STATS']._serialized_start = 435
    _globals['_POLICY_STATS']._serialized_end = 507
    _globals['_POLICY_BUFFER']._serialized_start = 509
    _globals['_POLICY_BUFFER']._serialized_end = 537
    _globals['_SYSTEMPOLICY']._serialized_start = 540
    _globals['_SYSTEMPOLICY']._serialized_end = 717
    _globals['_SYSTEMPOLICY_STATS']._serialized_start = 608
    _globals['_SYSTEMPOLICY_STATS']._serialized_end = 717
    _globals['_CONFIG']._serialized_start = 720
    _globals['_CONFIG']._serialized_end = 897
    _globals['_CONFIG_LEVELENTRY']._serialized_start = 828
    _globals['_CONFIG_LEVELENTRY']._serialized_end = 897
