# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xcapi/xray/app/dns/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from xcapi.xray.common.net.destination_pb import Endpoint
from xcapi.xray.app.router.config_pb import GeoIP
from xcapi.model import ClassMeta
from typing import Optional, List
from dataclasses import dataclass
from enum import Enum


class DomainMatchingType(Enum):
    Full: int = 0
    Subdomain: int = 1
    Keyword: int = 2
    Regex: int = 3


class QueryStrategy(Enum):
    USE_IP: int = 0
    USE_IP4: int = 1
    USE_IP6: int = 2


@dataclass
class NameServer(ClassMeta):
    address: Optional[Endpoint] = None
    client_ip: Optional[bytes] = None
    skipFallback: Optional[bool] = None

    @dataclass
    class PriorityDomain(ClassMeta):
        type: Optional[DomainMatchingType] = None
        domain: Optional[str] = None

    @dataclass
    class OriginalRule(ClassMeta):
        rule: Optional[str] = None
        size: Optional[int] = None

    prioritized_domain: Optional[List[PriorityDomain]] = None
    geoip: Optional[List[GeoIP]] = None
    original_rules: Optional[List[OriginalRule]] = None
    query_strategy: Optional[QueryStrategy] = None


@dataclass
class Config(ClassMeta):
    name_server: Optional[List[NameServer]] = None
    """
    NameServer list used by this DNS client.
    A special value 'localhost' as a domain address can be set to use DNS on local system.
    """
    client_ip: Optional[bytes] = None
    """Client IP for EDNS client subnet. Must be 4 bytes (IPv4) or 16 bytes (IPv6)."""

    @dataclass
    class HostMapping(ClassMeta):
        type: Optional[DomainMatchingType] = None
        domain: Optional[str] = None
        ip: Optional[List[bytes]] = None
        proxied_domain: Optional[str] = None
        """
        ProxiedDomain indicates the mapped domain has the same IP address on this
        domain. Xray will use this domain for IP queries.
        """

    static_hosts: Optional[List[HostMapping]] = None
    tag: Optional[str] = None
    """Tag is the inbound tag of DNS client."""
    disableCache: Optional[bool] = None
    """DisableCache disables DNS cache"""
    query_strategy: Optional[QueryStrategy] = None
    disableFallback: Optional[bool] = None
    disableFallbackIfMatch: Optional[bool] = None


_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1fxcapi/xray/app/dns/config.proto\x12\x0cxray.app.dns\x1a\'xcapi/xray/common/net/destination.proto\x1a\"xcapi/xray/app/router/config.proto\"\xbf\x03\n\nNameServer\x12*\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x19.xray.common.net.Endpoint\x12\x11\n\tclient_ip\x18\x05 \x01(\x0c\x12\x14\n\x0cskipFallback\x18\x06 \x01(\x08\x12\x43\n\x12prioritized_domain\x18\x02 \x03(\x0b\x32\'.xray.app.dns.NameServer.PriorityDomain\x12%\n\x05geoip\x18\x03 \x03(\x0b\x32\x16.xray.app.router.GeoIP\x12=\n\x0eoriginal_rules\x18\x04 \x03(\x0b\x32%.xray.app.dns.NameServer.OriginalRule\x12\x33\n\x0equery_strategy\x18\x07 \x01(\x0e\x32\x1b.xray.app.dns.QueryStrategy\x1aP\n\x0ePriorityDomain\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .xray.app.dns.DomainMatchingType\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x1a*\n\x0cOriginalRule\x12\x0c\n\x04rule\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\r\"\x8c\x03\n\x06\x43onfig\x12-\n\x0bname_server\x18\x05 \x03(\x0b\x32\x18.xray.app.dns.NameServer\x12\x11\n\tclient_ip\x18\x03 \x01(\x0c\x12\x36\n\x0cstatic_hosts\x18\x04 \x03(\x0b\x32 .xray.app.dns.Config.HostMapping\x12\x0b\n\x03tag\x18\x06 \x01(\t\x12\x14\n\x0c\x64isableCache\x18\x08 \x01(\x08\x12\x33\n\x0equery_strategy\x18\t \x01(\x0e\x32\x1b.xray.app.dns.QueryStrategy\x12\x17\n\x0f\x64isableFallback\x18\n \x01(\x08\x12\x1e\n\x16\x64isableFallbackIfMatch\x18\x0b \x01(\x08\x1aq\n\x0bHostMapping\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .xray.app.dns.DomainMatchingType\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\n\n\x02ip\x18\x03 \x03(\x0c\x12\x16\n\x0eproxied_domain\x18\x04 \x01(\tJ\x04\x08\x07\x10\x08*E\n\x12\x44omainMatchingType\x12\x08\n\x04\x46ull\x10\x00\x12\r\n\tSubdomain\x10\x01\x12\x0b\n\x07Keyword\x10\x02\x12\t\n\x05Regex\x10\x03*5\n\rQueryStrategy\x12\n\n\x06USE_IP\x10\x00\x12\x0b\n\x07USE_IP4\x10\x01\x12\x0b\n\x07USE_IP6\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xcapi.xray.app.dns.config_pb', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_DOMAINMATCHINGTYPE']._serialized_start = 975
    _globals['_DOMAINMATCHINGTYPE']._serialized_end = 1044
    _globals['_QUERYSTRATEGY']._serialized_start = 1046
    _globals['_QUERYSTRATEGY']._serialized_end = 1099
    _globals['_NAMESERVER']._serialized_start = 127
    _globals['_NAMESERVER']._serialized_end = 574
    _globals['_NAMESERVER_PRIORITYDOMAIN']._serialized_start = 450
    _globals['_NAMESERVER_PRIORITYDOMAIN']._serialized_end = 530
    _globals['_NAMESERVER_ORIGINALRULE']._serialized_start = 532
    _globals['_NAMESERVER_ORIGINALRULE']._serialized_end = 574
    _globals['_CONFIG']._serialized_start = 577
    _globals['_CONFIG']._serialized_end = 973
    _globals['_CONFIG_HOSTMAPPING']._serialized_start = 854
    _globals['_CONFIG_HOSTMAPPING']._serialized_end = 967