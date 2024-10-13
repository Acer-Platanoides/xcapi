# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xcapi/xray/app/observatory/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from typing import Optional, List
from xcapi.model import ClassMeta
from dataclasses import dataclass


@dataclass
class HealthPingMeasurementResult(ClassMeta):
    all: Optional[int] = None
    fail: Optional[int] = None
    deviation: Optional[int] = None
    average: Optional[int] = None
    max: Optional[int] = None
    min: Optional[int] = None


@dataclass
class OutboundStatus(ClassMeta):
    alive: Optional[bool] = None
    """Whether this outbound is usable"""
    delay: Optional[int] = None
    """The time for probe request to finish."""
    last_error_reason: Optional[str] = None
    """The last error caused this outbound failed to relay probe request"""
    outbound_tag: Optional[str] = None
    """The outbound tag for this Server"""
    last_seen_time: Optional[int] = None
    """The time this outbound is known to be alive"""
    last_try_time: Optional[int] = None
    """The time this outbound is tried"""
    health_ping: Optional[HealthPingMeasurementResult] = None


@dataclass
class ObservationResult(ClassMeta):
    status: Optional[List[OutboundStatus]] = None


@dataclass
class ProbeResult(ClassMeta):
    alive: Optional[bool] = None
    """Whether this outbound is usable"""
    delay: Optional[int] = None
    """The time for probe request to finish."""
    last_error_reason: Optional[str] = None
    """The error caused this outbound failed to relay probe request"""


@dataclass
class Intensity(ClassMeta):
    probe_interval: Optional[int] = None
    """The time interval for a probe request in ms."""


@dataclass
class Config(ClassMeta):
    subject_selector: Optional[List[str]] = None
    """The selectors for outbound under observation"""
    probe_url: Optional[str] = None
    probe_interval: Optional[int] = None
    enable_concurrency: Optional[bool] = None


_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\'xcapi/xray/app/observatory/config.proto\x12\x19xray.core.app.observatory\"N\n\x11ObservationResult\x12\x39\n\x06status\x18\x01 \x03(\x0b\x32).xray.core.app.observatory.OutboundStatus\"v\n\x1bHealthPingMeasurementResult\x12\x0b\n\x03\x61ll\x18\x01 \x01(\x03\x12\x0c\n\x04\x66\x61il\x18\x02 \x01(\x03\x12\x11\n\tdeviation\x18\x03 \x01(\x03\x12\x0f\n\x07\x61verage\x18\x04 \x01(\x03\x12\x0b\n\x03max\x18\x05 \x01(\x03\x12\x0b\n\x03min\x18\x06 \x01(\x03\"\xdb\x01\n\x0eOutboundStatus\x12\r\n\x05\x61live\x18\x01 \x01(\x08\x12\r\n\x05\x64\x65lay\x18\x02 \x01(\x03\x12\x19\n\x11last_error_reason\x18\x03 \x01(\t\x12\x14\n\x0coutbound_tag\x18\x04 \x01(\t\x12\x16\n\x0elast_seen_time\x18\x05 \x01(\x03\x12\x15\n\rlast_try_time\x18\x06 \x01(\x03\x12K\n\x0bhealth_ping\x18\x07 \x01(\x0b\x32\x36.xray.core.app.observatory.HealthPingMeasurementResult\"F\n\x0bProbeResult\x12\r\n\x05\x61live\x18\x01 \x01(\x08\x12\r\n\x05\x64\x65lay\x18\x02 \x01(\x03\x12\x19\n\x11last_error_reason\x18\x03 \x01(\t\"#\n\tIntensity\x12\x16\n\x0eprobe_interval\x18\x01 \x01(\r\"i\n\x06\x43onfig\x12\x18\n\x10subject_selector\x18\x02 \x03(\t\x12\x11\n\tprobe_url\x18\x03 \x01(\t\x12\x16\n\x0eprobe_interval\x18\x04 \x01(\x03\x12\x1a\n\x12\x65nable_concurrency\x18\x05 \x01(\x08\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xcapi.xray.app.observatory.config_pb', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_OBSERVATIONRESULT']._serialized_start = 70
    _globals['_OBSERVATIONRESULT']._serialized_end = 148
    _globals['_HEALTHPINGMEASUREMENTRESULT']._serialized_start = 150
    _globals['_HEALTHPINGMEASUREMENTRESULT']._serialized_end = 268
    _globals['_OUTBOUNDSTATUS']._serialized_start = 271
    _globals['_OUTBOUNDSTATUS']._serialized_end = 490
    _globals['_PROBERESULT']._serialized_start = 492
    _globals['_PROBERESULT']._serialized_end = 562
    _globals['_INTENSITY']._serialized_start = 564
    _globals['_INTENSITY']._serialized_end = 599
    _globals['_CONFIG']._serialized_start = 601
    _globals['_CONFIG']._serialized_end = 706