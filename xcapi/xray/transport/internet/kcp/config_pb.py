# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xcapi/xray/transport/internet/kcp/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from xcapi.xray.common.serial.typed_message_pb import TypedMessage
from typing import Optional
from xcapi.model import ClassMeta
from dataclasses import dataclass


@dataclass
class MTU(ClassMeta):
    """Maximum Transmission Unit, in bytes."""
    value: Optional[int] = None


@dataclass
class TTI(ClassMeta):
    """Transmission Time Interview, in milli-sec."""
    value: Optional[int] = None


@dataclass
class UplinkCapacity(ClassMeta):
    """Uplink capacity, in MB."""
    value: Optional[int] = None


@dataclass
class DownlinkCapacity(ClassMeta):
    """Downlink capacity, in MB."""
    value: Optional[int] = None


@dataclass
class WriteBuffer(ClassMeta):
    size: Optional[int] = None
    """Buffer size in bytes."""


@dataclass
class ReadBuffer(ClassMeta):
    size: Optional[int] = None
    """Buffer size in bytes."""


@dataclass
class ConnectionReuse(ClassMeta):
    enable: Optional[bool] = None


@dataclass
class EncryptionSeed(ClassMeta):
    """Maximum Transmission Unit, in bytes."""
    seed: Optional[str] = None


@dataclass
class Config(ClassMeta):
    mtu: Optional[MTU] = None
    tti: Optional[TTI] = None
    uplink_capacity: Optional[UplinkCapacity] = None
    downlink_capacity: Optional[DownlinkCapacity] = None
    congestion: Optional[bool] = None
    write_buffer: Optional[WriteBuffer] = None
    read_buffer: Optional[ReadBuffer] = None
    header_config: Optional[TypedMessage] = None
    seed: Optional[EncryptionSeed] = None


_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n.xcapi/xray/transport/internet/kcp/config.proto\x12\x1bxray.transport.internet.kcp\x1a,xcapi/xray/common/serial/typed_message.proto\"\x14\n\x03MTU\x12\r\n\x05value\x18\x01 \x01(\r\"\x14\n\x03TTI\x12\r\n\x05value\x18\x01 \x01(\r\"\x1f\n\x0eUplinkCapacity\x12\r\n\x05value\x18\x01 \x01(\r\"!\n\x10\x44ownlinkCapacity\x12\r\n\x05value\x18\x01 \x01(\r\"\x1b\n\x0bWriteBuffer\x12\x0c\n\x04size\x18\x01 \x01(\r\"\x1a\n\nReadBuffer\x12\x0c\n\x04size\x18\x01 \x01(\r\"!\n\x0f\x43onnectionReuse\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\"\x1e\n\x0e\x45ncryptionSeed\x12\x0c\n\x04seed\x18\x01 \x01(\t\"\x82\x04\n\x06\x43onfig\x12-\n\x03mtu\x18\x01 \x01(\x0b\x32 .xray.transport.internet.kcp.MTU\x12-\n\x03tti\x18\x02 \x01(\x0b\x32 .xray.transport.internet.kcp.TTI\x12\x44\n\x0fuplink_capacity\x18\x03 \x01(\x0b\x32+.xray.transport.internet.kcp.UplinkCapacity\x12H\n\x11\x64ownlink_capacity\x18\x04 \x01(\x0b\x32-.xray.transport.internet.kcp.DownlinkCapacity\x12\x12\n\ncongestion\x18\x05 \x01(\x08\x12>\n\x0cwrite_buffer\x18\x06 \x01(\x0b\x32(.xray.transport.internet.kcp.WriteBuffer\x12<\n\x0bread_buffer\x18\x07 \x01(\x0b\x32\'.xray.transport.internet.kcp.ReadBuffer\x12\x37\n\rheader_config\x18\x08 \x01(\x0b\x32 .xray.common.serial.TypedMessage\x12\x39\n\x04seed\x18\n \x01(\x0b\x32+.xray.transport.internet.kcp.EncryptionSeedJ\x04\x08\t\x10\nb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xcapi.xray.transport.internet.kcp.config_pb', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_MTU']._serialized_start = 125
    _globals['_MTU']._serialized_end = 145
    _globals['_TTI']._serialized_start = 147
    _globals['_TTI']._serialized_end = 167
    _globals['_UPLINKCAPACITY']._serialized_start = 169
    _globals['_UPLINKCAPACITY']._serialized_end = 200
    _globals['_DOWNLINKCAPACITY']._serialized_start = 202
    _globals['_DOWNLINKCAPACITY']._serialized_end = 235
    _globals['_WRITEBUFFER']._serialized_start = 237
    _globals['_WRITEBUFFER']._serialized_end = 264
    _globals['_READBUFFER']._serialized_start = 266
    _globals['_READBUFFER']._serialized_end = 292
    _globals['_CONNECTIONREUSE']._serialized_start = 294
    _globals['_CONNECTIONREUSE']._serialized_end = 327
    _globals['_ENCRYPTIONSEED']._serialized_start = 329
    _globals['_ENCRYPTIONSEED']._serialized_end = 359
    _globals['_CONFIG']._serialized_start = 362
    _globals['_CONFIG']._serialized_end = 876
