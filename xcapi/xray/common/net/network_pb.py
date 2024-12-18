# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xcapi/xray/common/net/network.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from xcapi.model import ClassMeta
from typing import Optional, List
from dataclasses import dataclass
from enum import Enum


class Network(Enum):
    Unknown: int = 0
    TCP: int = 2
    UDP: int = 3
    UNIX: int = 4


@dataclass
class NetworkList(ClassMeta):
    """NetworkList is a list of Networks."""
    network: Optional[List[Network]] = None


_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n#xcapi/xray/common/net/network.proto\x12\x0fxray.common.net\"8\n\x0bNetworkList\x12)\n\x07network\x18\x01 \x03(\x0e\x32\x18.xray.common.net.Network*2\n\x07Network\x12\x0b\n\x07Unknown\x10\x00\x12\x07\n\x03TCP\x10\x02\x12\x07\n\x03UDP\x10\x03\x12\x08\n\x04UNIX\x10\x04\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xcapi.xray.common.net.network_pb', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_NETWORK']._serialized_start = 114
    _globals['_NETWORK']._serialized_end = 164
    _globals['_NETWORKLIST']._serialized_start = 56
    _globals['_NETWORKLIST']._serialized_end = 112
