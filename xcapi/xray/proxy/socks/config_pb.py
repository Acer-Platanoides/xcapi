# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xcapi/xray/proxy/socks/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from typing import Optional, Dict, List
from dataclasses import dataclass
from xcapi.model import ClassMeta
from xcapi.xray.common.protocol.server_spec_pb import ServerEndpoint
from enum import Enum
from xcapi.xray.common.net.address_pb import IPOrDomain


@dataclass
class Account(ClassMeta):
    """Account represents a Socks account."""
    username: Optional[str] = None
    password: Optional[str] = None


class AuthType(Enum):
    """AuthType is the authentication type of Socks proxy."""
    NO_AUTH: int = 0
    """NO_AUTH is for anonymous authentication."""
    PASSWORD: int = 1
    """PASSWORD is for username/password authentication."""


@dataclass
class ServerConfig(ClassMeta):
    """ServerConfig is the protobuf config for Socks server."""
    auth_type: Optional[AuthType] = None
    accounts: Optional[Dict[str, str]] = None
    address: Optional[IPOrDomain] = None
    udp_enabled: Optional[bool] = None
    user_level: Optional[int] = None


class ClientConfig(ClassMeta):
    """ClientConfig is the protobuf config for Socks client."""
    server: Optional[List[ServerEndpoint]] = None
    """Sever is a list of Socks server addresses."""


_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n#xcapi/xray/proxy/socks/config.proto\x12\x10xray.proxy.socks\x1a#xcapi/xray/common/net/address.proto\x1a,xcapi/xray/common/protocol/server_spec.proto\"-\n\x07\x41\x63\x63ount\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x85\x02\n\x0cServerConfig\x12-\n\tauth_type\x18\x01 \x01(\x0e\x32\x1a.xray.proxy.socks.AuthType\x12>\n\x08\x61\x63\x63ounts\x18\x02 \x03(\x0b\x32,.xray.proxy.socks.ServerConfig.AccountsEntry\x12,\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x1b.xray.common.net.IPOrDomain\x12\x13\n\x0budp_enabled\x18\x04 \x01(\x08\x12\x12\n\nuser_level\x18\x06 \x01(\r\x1a/\n\rAccountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"D\n\x0c\x43lientConfig\x12\x34\n\x06server\x18\x01 \x03(\x0b\x32$.xray.common.protocol.ServerEndpoint*%\n\x08\x41uthType\x12\x0b\n\x07NO_AUTH\x10\x00\x12\x0c\n\x08PASSWORD\x10\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xcapi.xray.proxy.socks.config_pb', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_SERVERCONFIG_ACCOUNTSENTRY']._loaded_options = None
    _globals['_SERVERCONFIG_ACCOUNTSENTRY']._serialized_options = b'8\001'
    _globals['_AUTHTYPE']._serialized_start = 521
    _globals['_AUTHTYPE']._serialized_end = 558
    _globals['_ACCOUNT']._serialized_start = 140
    _globals['_ACCOUNT']._serialized_end = 185
    _globals['_SERVERCONFIG']._serialized_start = 188
    _globals['_SERVERCONFIG']._serialized_end = 449
    _globals['_SERVERCONFIG_ACCOUNTSENTRY']._serialized_start = 402
    _globals['_SERVERCONFIG_ACCOUNTSENTRY']._serialized_end = 449
    _globals['_CLIENTCONFIG']._serialized_start = 451
    _globals['_CLIENTCONFIG']._serialized_end = 519
