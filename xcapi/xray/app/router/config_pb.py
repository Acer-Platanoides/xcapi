# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xcapi/xray/app/router/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from xcapi.xray.common.serial.typed_message_pb import TypedMessage
from xcapi.xray.common.net.port_pb import PortList
from xcapi.xray.common.net.network_pb import Network
from xcapi.model import ClassMeta
from typing import Optional, List, Dict
from dataclasses import dataclass
from enum import Enum


@dataclass
class Domain(ClassMeta):
    """Domain for routing decision."""

    class Type(Enum):
        """Type of domain value."""
        Plain: int = 0
        """The value is used as is."""
        Regex: int = 1
        """The value is used as a regular expression."""
        Domain: int = 2
        """The value is a root domain."""
        Full: int = 3
        """The value is a domain."""

    type: Optional[Type] = None
    """Domain matching type."""
    value: Optional[str] = None
    """Domain value."""

    @dataclass
    class Attribute(ClassMeta):
        key: Optional[str] = None
        bool_value: Optional[bool] = None
        int_value: Optional[int] = None

    attribute: Optional[List[Attribute]] = None
    """Attributes of this domain. May be used for filtering."""


@dataclass
class CIDR(ClassMeta):
    """IP for routing decision, in CIDR form."""
    ip: Optional[bytes] = None
    """IP address, should be either 4 or 16 bytes."""
    prefix: Optional[int] = None
    """Number of leading ones in the network mask."""


@dataclass
class GeoIP(ClassMeta):
    country_code: Optional[str] = None
    cidr: Optional[List[CIDR]] = None
    reverse_match: Optional[bool] = None


@dataclass
class GeoIPList(ClassMeta):
    entry: Optional[List[GeoIP]] = None


@dataclass
class GeoSite(ClassMeta):
    country_code: Optional[str] = None
    domain: Optional[List[Domain]] = None


@dataclass
class GeoSiteList(ClassMeta):
    entry: Optional[List[GeoSite]] = None


@dataclass
class RoutingRule(ClassMeta):
    tag: Optional[str] = None
    """Tag of outbound that this rule is pointing to."""
    balancing_tag: Optional[str] = None
    """Tag of routing balancer."""
    rule_tag: Optional[str] = None
    domain: Optional[List[Domain]] = None
    """List of domains for target domain matching."""
    geoip: Optional[List[GeoIP]] = None
    """
    List of GeoIPs for target IP address matching. If this entry exists, the cidr above will have no effect.
    GeoIP fields with the same country code are supposed to contain exactly same content.
    They will be merged during runtime. For customized GeoIPs, please leave country code empty.
    """
    port_list: Optional[PortList] = None
    """List of ports."""
    networks: Optional[List[Network]] = None
    """List of networks for matching."""
    source_geoip: Optional[List[GeoIP]] = None
    """List of GeoIPs for source IP address matching. If this entry exists, the source_cidr above will have no effect."""
    source_port_list: Optional[PortList] = None
    """List of ports for source port matching."""
    user_email: Optional[List[str]] = None
    inbound_tag: Optional[List[str]] = None
    protocol: Optional[List[str]] = None
    attributes: Optional[Dict[str, str]] = None
    domain_matcher: Optional[str] = None


@dataclass
class BalancingRule(ClassMeta):
    tag: Optional[str] = None
    outbound_selector: Optional[List[str]] = None
    strategy: Optional[str] = None
    strategy_settings: Optional[TypedMessage] = None
    fallback_tag: Optional[str] = None


@dataclass
class StrategyWeight(ClassMeta):
    regexp: Optional[bool] = None
    match: Optional[str] = None
    value: Optional[float] = None


@dataclass
class StrategyLeastLoadConfig(ClassMeta):
    costs: Optional[List[StrategyWeight]] = None
    """weight settings"""
    baselines: Optional[List[int]] = None
    """RTT baselines for selecting, int64 values of time.Duration"""
    expected: Optional[int] = None
    """expected nodes count to select"""
    maxRTT: Optional[int] = None
    """max acceptable rtt, filter away high delay nodes. default 0"""
    tolerance: Optional[float] = None
    """acceptable failure rate"""


@dataclass
class Config(ClassMeta):
    class DomainStrategy(Enum):
        AsIs: int = 0
        """Use domain as is."""
        UseIp: int = 1
        """Always resolve IP for domains."""
        IpIfNonMatch: int = 2
        """Resolve to IP if the domain doesn't match any rules."""
        IpOnDemand: int = 3
        """Resolve to IP if any rule requires IP matching."""

    domain_strategy: Optional[DomainStrategy] = None
    rule: Optional[List[RoutingRule]] = None
    balancing_rule: Optional[List[BalancingRule]] = None


_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\"xcapi/xray/app/router/config.proto\x12\x0fxray.app.router\x1a,xcapi/xray/common/serial/typed_message.proto\x1a xcapi/xray/common/net/port.proto\x1a#xcapi/xray/common/net/network.proto\"\x81\x02\n\x06\x44omain\x12*\n\x04type\x18\x01 \x01(\x0e\x32\x1c.xray.app.router.Domain.Type\x12\r\n\x05value\x18\x02 \x01(\t\x12\x34\n\tattribute\x18\x03 \x03(\x0b\x32!.xray.app.router.Domain.Attribute\x1aR\n\tAttribute\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x14\n\nbool_value\x18\x02 \x01(\x08H\x00\x12\x13\n\tint_value\x18\x03 \x01(\x03H\x00\x42\r\n\x0btyped_value\"2\n\x04Type\x12\t\n\x05Plain\x10\x00\x12\t\n\x05Regex\x10\x01\x12\n\n\x06\x44omain\x10\x02\x12\x08\n\x04\x46ull\x10\x03\"\"\n\x04\x43IDR\x12\n\n\x02ip\x18\x01 \x01(\x0c\x12\x0e\n\x06prefix\x18\x02 \x01(\r\"Y\n\x05GeoIP\x12\x14\n\x0c\x63ountry_code\x18\x01 \x01(\t\x12#\n\x04\x63idr\x18\x02 \x03(\x0b\x32\x15.xray.app.router.CIDR\x12\x15\n\rreverse_match\x18\x03 \x01(\x08\"2\n\tGeoIPList\x12%\n\x05\x65ntry\x18\x01 \x03(\x0b\x32\x16.xray.app.router.GeoIP\"H\n\x07GeoSite\x12\x14\n\x0c\x63ountry_code\x18\x01 \x01(\t\x12\'\n\x06\x64omain\x18\x02 \x03(\x0b\x32\x17.xray.app.router.Domain\"6\n\x0bGeoSiteList\x12\'\n\x05\x65ntry\x18\x01 \x03(\x0b\x32\x18.xray.app.router.GeoSite\"\xaa\x04\n\x0bRoutingRule\x12\r\n\x03tag\x18\x01 \x01(\tH\x00\x12\x17\n\rbalancing_tag\x18\x0c \x01(\tH\x00\x12\x10\n\x08rule_tag\x18\x12 \x01(\t\x12\'\n\x06\x64omain\x18\x02 \x03(\x0b\x32\x17.xray.app.router.Domain\x12%\n\x05geoip\x18\n \x03(\x0b\x32\x16.xray.app.router.GeoIP\x12,\n\tport_list\x18\x0e \x01(\x0b\x32\x19.xray.common.net.PortList\x12*\n\x08networks\x18\r \x03(\x0e\x32\x18.xray.common.net.Network\x12,\n\x0csource_geoip\x18\x0b \x03(\x0b\x32\x16.xray.app.router.GeoIP\x12\x33\n\x10source_port_list\x18\x10 \x01(\x0b\x32\x19.xray.common.net.PortList\x12\x12\n\nuser_email\x18\x07 \x03(\t\x12\x13\n\x0binbound_tag\x18\x08 \x03(\t\x12\x10\n\x08protocol\x18\t \x03(\t\x12@\n\nattributes\x18\x0f \x03(\x0b\x32,.xray.app.router.RoutingRule.AttributesEntry\x12\x16\n\x0e\x64omain_matcher\x18\x11 \x01(\t\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x0c\n\ntarget_tag\"\x9c\x01\n\rBalancingRule\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x19\n\x11outbound_selector\x18\x02 \x03(\t\x12\x10\n\x08strategy\x18\x03 \x01(\t\x12;\n\x11strategy_settings\x18\x04 \x01(\x0b\x32 .xray.common.serial.TypedMessage\x12\x14\n\x0c\x66\x61llback_tag\x18\x05 \x01(\t\">\n\x0eStrategyWeight\x12\x0e\n\x06regexp\x18\x01 \x01(\x08\x12\r\n\x05match\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x02\"\x91\x01\n\x17StrategyLeastLoadConfig\x12.\n\x05\x63osts\x18\x02 \x03(\x0b\x32\x1f.xray.app.router.StrategyWeight\x12\x11\n\tbaselines\x18\x03 \x03(\x03\x12\x10\n\x08\x65xpected\x18\x04 \x01(\x05\x12\x0e\n\x06maxRTT\x18\x05 \x01(\x03\x12\x11\n\ttolerance\x18\x06 \x01(\x02\"\xf6\x01\n\x06\x43onfig\x12?\n\x0f\x64omain_strategy\x18\x01 \x01(\x0e\x32&.xray.app.router.Config.DomainStrategy\x12*\n\x04rule\x18\x02 \x03(\x0b\x32\x1c.xray.app.router.RoutingRule\x12\x36\n\x0e\x62\x61lancing_rule\x18\x03 \x03(\x0b\x32\x1e.xray.app.router.BalancingRule\"G\n\x0e\x44omainStrategy\x12\x08\n\x04\x41sIs\x10\x00\x12\t\n\x05UseIp\x10\x01\x12\x10\n\x0cIpIfNonMatch\x10\x02\x12\x0e\n\nIpOnDemand\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xcapi.xray.app.router.config_pb', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_ROUTINGRULE_ATTRIBUTESENTRY']._loaded_options = None
    _globals['_ROUTINGRULE_ATTRIBUTESENTRY']._serialized_options = b'8\001'
    _globals['_DOMAIN']._serialized_start = 173
    _globals['_DOMAIN']._serialized_end = 430
    _globals['_DOMAIN_ATTRIBUTE']._serialized_start = 296
    _globals['_DOMAIN_ATTRIBUTE']._serialized_end = 378
    _globals['_DOMAIN_TYPE']._serialized_start = 380
    _globals['_DOMAIN_TYPE']._serialized_end = 430
    _globals['_CIDR']._serialized_start = 432
    _globals['_CIDR']._serialized_end = 466
    _globals['_GEOIP']._serialized_start = 468
    _globals['_GEOIP']._serialized_end = 557
    _globals['_GEOIPLIST']._serialized_start = 559
    _globals['_GEOIPLIST']._serialized_end = 609
    _globals['_GEOSITE']._serialized_start = 611
    _globals['_GEOSITE']._serialized_end = 683
    _globals['_GEOSITELIST']._serialized_start = 685
    _globals['_GEOSITELIST']._serialized_end = 739
    _globals['_ROUTINGRULE']._serialized_start = 742
    _globals['_ROUTINGRULE']._serialized_end = 1296
    _globals['_ROUTINGRULE_ATTRIBUTESENTRY']._serialized_start = 1233
    _globals['_ROUTINGRULE_ATTRIBUTESENTRY']._serialized_end = 1282
    _globals['_BALANCINGRULE']._serialized_start = 1299
    _globals['_BALANCINGRULE']._serialized_end = 1455
    _globals['_STRATEGYWEIGHT']._serialized_start = 1457
    _globals['_STRATEGYWEIGHT']._serialized_end = 1519
    _globals['_STRATEGYLEASTLOADCONFIG']._serialized_start = 1522
    _globals['_STRATEGYLEASTLOADCONFIG']._serialized_end = 1667
    _globals['_CONFIG']._serialized_start = 1670
    _globals['_CONFIG']._serialized_end = 1916
    _globals['_CONFIG_DOMAINSTRATEGY']._serialized_start = 1845
    _globals['_CONFIG_DOMAINSTRATEGY']._serialized_end = 1916
