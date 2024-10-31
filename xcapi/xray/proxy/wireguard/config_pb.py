# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xcapi/xray/proxy/wireguard/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from typing import Optional, List
from dataclasses import dataclass
from xcapi.model import ClassMeta
from enum import Enum


@dataclass
class PeerConfig(ClassMeta):
    public_key: Optional[str] = None
    pre_shared_key: Optional[str] = None
    endpoint: Optional[str] = None
    keep_alive: Optional[int] = None
    allowed_ips: Optional[List[str]] = None


@dataclass
class DeviceConfig(ClassMeta):
    class DomainStrategy(Enum):
        FORCE_IP: int = 0
        FORCE_IP4: int = 1
        FORCE_IP6: int = 2
        FORCE_IP46: int = 3
        FORCE_IP64: int = 4

    secret_key: Optional[str] = None
    endpoint: Optional[List[str]] = None
    peers: Optional[List[PeerConfig]] = None
    mtu: Optional[int] = None
    num_workers: Optional[int] = None
    reserved: Optional[bytes] = None
    domain_strategy: Optional[DomainStrategy] = None
    is_client: Optional[bool] = None
    no_kernel_tun: Optional[bool] = None


_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\'xcapi/xray/proxy/wireguard/config.proto\x12\x14xray.proxy.wireguard\"s\n\nPeerConfig\x12\x12\n\npublic_key\x18\x01 \x01(\t\x12\x16\n\x0epre_shared_key\x18\x02 \x01(\t\x12\x10\n\x08\x65ndpoint\x18\x03 \x01(\t\x12\x12\n\nkeep_alive\x18\x04 \x01(\r\x12\x13\n\x0b\x61llowed_ips\x18\x05 \x03(\t\"\xed\x02\n\x0c\x44\x65viceConfig\x12\x12\n\nsecret_key\x18\x01 \x01(\t\x12\x10\n\x08\x65ndpoint\x18\x02 \x03(\t\x12/\n\x05peers\x18\x03 \x03(\x0b\x32 .xray.proxy.wireguard.PeerConfig\x12\x0b\n\x03mtu\x18\x04 \x01(\x05\x12\x13\n\x0bnum_workers\x18\x05 \x01(\x05\x12\x10\n\x08reserved\x18\x06 \x01(\x0c\x12J\n\x0f\x64omain_strategy\x18\x07 \x01(\x0e\x32\x31.xray.proxy.wireguard.DeviceConfig.DomainStrategy\x12\x11\n\tis_client\x18\x08 \x01(\x08\x12\x15\n\rno_kernel_tun\x18\t \x01(\x08\"\\\n\x0e\x44omainStrategy\x12\x0c\n\x08\x46ORCE_IP\x10\x00\x12\r\n\tFORCE_IP4\x10\x01\x12\r\n\tFORCE_IP6\x10\x02\x12\x0e\n\nFORCE_IP46\x10\x03\x12\x0e\n\nFORCE_IP64\x10\x04\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xcapi.xray.proxy.wireguard.config_pb', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_PEERCONFIG']._serialized_start = 65
    _globals['_PEERCONFIG']._serialized_end = 180
    _globals['_DEVICECONFIG']._serialized_start = 183
    _globals['_DEVICECONFIG']._serialized_end = 548
    _globals['_DEVICECONFIG_DOMAINSTRATEGY']._serialized_start = 456
    _globals['_DEVICECONFIG_DOMAINSTRATEGY']._serialized_end = 548
