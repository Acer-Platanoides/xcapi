# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xcapi/xray/app/observatory/burst/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from typing import Optional, List
from xcapi.model import ClassMeta
from dataclasses import dataclass


@dataclass
class HealthPingConfig(ClassMeta):
    destination: Optional[str] = None
    """
    destination url, need 204 for success return
    default https://connectivitycheck.gstatic.com/generate_204
    """
    connectivity: Optional[str] = None
    """connectivity check url"""
    interval: Optional[int] = None
    """health check interval, int64 values of time.Duration"""
    samplingCount: Optional[int] = None
    """sampling count is the amount of recent ping results which are kept for calculation"""
    timeout: Optional[int] = None
    """ping timeout, int64 values of time.Duration"""


@dataclass
class Config(ClassMeta):
    subject_selector: Optional[List[str]] = None
    """The selectors for outbound under observation"""
    ping_config: Optional[HealthPingConfig] = None


_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n-xcapi/xray/app/observatory/burst/config.proto\x12\x1fxray.core.app.observatory.burst\"j\n\x06\x43onfig\x12\x18\n\x10subject_selector\x18\x02 \x03(\t\x12\x46\n\x0bping_config\x18\x03 \x01(\x0b\x32\x31.xray.core.app.observatory.burst.HealthPingConfig\"w\n\x10HealthPingConfig\x12\x13\n\x0b\x64\x65stination\x18\x01 \x01(\t\x12\x14\n\x0c\x63onnectivity\x18\x02 \x01(\t\x12\x10\n\x08interval\x18\x03 \x01(\x03\x12\x15\n\rsamplingCount\x18\x04 \x01(\x05\x12\x0f\n\x07timeout\x18\x05 \x01(\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xcapi.xray.app.observatory.burst.config_pb', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_CONFIG']._serialized_start = 82
    _globals['_CONFIG']._serialized_end = 188
    _globals['_HEALTHPINGCONFIG']._serialized_start = 190
    _globals['_HEALTHPINGCONFIG']._serialized_end = 309