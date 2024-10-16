# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xcapi/xray/common/protocol/user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from typing import Optional
from dataclasses import dataclass
from xcapi.xray.common.serial.typed_message_pb import TypedMessage
from xcapi.model import ClassMeta


@dataclass
class User(ClassMeta):
    """User is a generic user for all protocols."""
    level: Optional[int] = None
    email: Optional[str] = None
    account: Optional[TypedMessage] = None
    """Protocol specific account information. Must be the account proto in one of the proxies."""


_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n%xcapi/xray/common/protocol/user.proto\x12\x14xray.common.protocol\x1a,xcapi/xray/common/serial/typed_message.proto\"W\n\x04User\x12\r\n\x05level\x18\x01 \x01(\r\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x31\n\x07\x61\x63\x63ount\x18\x03 \x01(\x0b\x32 .xray.common.serial.TypedMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xcapi.xray.common.protocol.user_pb', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_USER']._serialized_start = 109
    _globals['_USER']._serialized_end = 196
