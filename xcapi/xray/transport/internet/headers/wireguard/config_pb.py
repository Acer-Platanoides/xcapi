# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xcapi/xray/transport/internet/headers/wireguard/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from xcapi.model import ClassMeta
from dataclasses import dataclass


@dataclass
class WireguardConfig(ClassMeta):
    pass


_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n<xcapi/xray/transport/internet/headers/wireguard/config.proto\x12)xray.transport.internet.headers.wireguard\"\x11\n\x0fWireguardConfigb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xcapi.xray.transport.internet.headers.wireguard.config_pb', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_WIREGUARDCONFIG']._serialized_start = 107
    _globals['_WIREGUARDCONFIG']._serialized_end = 124
