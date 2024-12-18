# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xcapi/xray/core/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from typing import List, Optional
from dataclasses import dataclass
from xcapi.xray.common.serial.typed_message_pb import TypedMessage
from xcapi.model import ClassMeta


@dataclass
class InboundHandlerConfig(ClassMeta):
    """InboundHandlerConfig is the configuration for inbound handler."""
    tag: Optional[str] = None
    """Tag of the inbound handler. The tag must be unique among all inbound handlers"""
    receiver_settings: Optional[TypedMessage] = None
    """Settings for how this inbound proxy is handled."""
    proxy_settings: Optional[TypedMessage] = None
    """Settings for inbound proxy. Must be one of the inbound proxies."""


@dataclass
class OutboundHandlerConfig(ClassMeta):
    """OutboundHandlerConfig is the configuration for outbound handler."""
    tag: Optional[str] = None
    """Tag of this outbound handler."""
    sender_settings: Optional[TypedMessage] = None
    """Settings for how to dial connection for this outbound handler."""
    proxy_settings: Optional[TypedMessage] = None
    """Settings for this outbound proxy. Must be one of the outbound proxies."""
    expire: Optional[int] = None
    """If not zero, this outbound will be expired in seconds. Not used for now."""
    comment: Optional[str] = None
    """Comment of this outbound handler. Not used for now."""


@dataclass
class Config(ClassMeta):
    """Config is the master config of Xray. Xray takes this config as input and functions accordingly."""
    inbound: Optional[List[InboundHandlerConfig]] = None
    """Inbound handler configurations. Must have at least one item."""
    outbound: Optional[List[OutboundHandlerConfig]] = None
    """Outbound handler configurations. Must have at least one item. The first item is used as default for routing."""
    app: Optional[List[TypedMessage]] = None
    """App is for configurations of all features in Xray. A feature must 
    implement the Feature interface, and its config type must be registered
    through common.RegisterConfig.
    """
    extension: Optional[List[TypedMessage]] = None
    """
    Configuration for extensions. The config may not work if corresponding
    extension is not loaded into Xray. Xray will ignore such config during
    initialization.
    """


_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1cxcapi/xray/core/config.proto\x12\txray.core\x1a,xcapi/xray/common/serial/typed_message.proto\"\xd8\x01\n\x06\x43onfig\x12\x30\n\x07inbound\x18\x01 \x03(\x0b\x32\x1f.xray.core.InboundHandlerConfig\x12\x32\n\x08outbound\x18\x02 \x03(\x0b\x32 .xray.core.OutboundHandlerConfig\x12-\n\x03\x61pp\x18\x04 \x03(\x0b\x32 .xray.common.serial.TypedMessage\x12\x33\n\textension\x18\x06 \x03(\x0b\x32 .xray.common.serial.TypedMessageJ\x04\x08\x03\x10\x04\"\x9a\x01\n\x14InboundHandlerConfig\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12;\n\x11receiver_settings\x18\x02 \x01(\x0b\x32 .xray.common.serial.TypedMessage\x12\x38\n\x0eproxy_settings\x18\x03 \x01(\x0b\x32 .xray.common.serial.TypedMessage\"\xba\x01\n\x15OutboundHandlerConfig\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x39\n\x0fsender_settings\x18\x02 \x01(\x0b\x32 .xray.common.serial.TypedMessage\x12\x38\n\x0eproxy_settings\x18\x03 \x01(\x0b\x32 .xray.common.serial.TypedMessage\x12\x0e\n\x06\x65xpire\x18\x04 \x01(\x03\x12\x0f\n\x07\x63omment\x18\x05 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xcapi.xray.core.config_pb', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_CONFIG']._serialized_start = 90
    _globals['_CONFIG']._serialized_end = 306
    _globals['_INBOUNDHANDLERCONFIG']._serialized_start = 309
    _globals['_INBOUNDHANDLERCONFIG']._serialized_end = 463
    _globals['_OUTBOUNDHANDLERCONFIG']._serialized_start = 466
    _globals['_OUTBOUNDHANDLERCONFIG']._serialized_end = 652
