# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ydb_monitoring_v1.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ydb._grpc.protos import ydb_monitoring_pb2 as protos_dot_ydb__monitoring__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ydb_monitoring_v1.proto',
  package='Ydb.Monitoring.V1',
  syntax='proto3',
  serialized_options=b'\n\026tech.ydb.monitoring.v1Z9github.com/ydb-platform/ydb-go-genproto/Ydb_Monitoring_V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17ydb_monitoring_v1.proto\x12\x11Ydb.Monitoring.V1\x1a\x1bprotos/ydb_monitoring.proto2\xb7\x01\n\x11MonitoringService\x12P\n\tSelfCheck\x12 .Ydb.Monitoring.SelfCheckRequest\x1a!.Ydb.Monitoring.SelfCheckResponse\x12P\n\tNodeCheck\x12 .Ydb.Monitoring.NodeCheckRequest\x1a!.Ydb.Monitoring.NodeCheckResponseBS\n\x16tech.ydb.monitoring.v1Z9github.com/ydb-platform/ydb-go-genproto/Ydb_Monitoring_V1b\x06proto3'
  ,
  dependencies=[protos_dot_ydb__monitoring__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_MONITORINGSERVICE = _descriptor.ServiceDescriptor(
  name='MonitoringService',
  full_name='Ydb.Monitoring.V1.MonitoringService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=76,
  serialized_end=259,
  methods=[
  _descriptor.MethodDescriptor(
    name='SelfCheck',
    full_name='Ydb.Monitoring.V1.MonitoringService.SelfCheck',
    index=0,
    containing_service=None,
    input_type=protos_dot_ydb__monitoring__pb2._SELFCHECKREQUEST,
    output_type=protos_dot_ydb__monitoring__pb2._SELFCHECKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='NodeCheck',
    full_name='Ydb.Monitoring.V1.MonitoringService.NodeCheck',
    index=1,
    containing_service=None,
    input_type=protos_dot_ydb__monitoring__pb2._NODECHECKREQUEST,
    output_type=protos_dot_ydb__monitoring__pb2._NODECHECKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MONITORINGSERVICE)

DESCRIPTOR.services_by_name['MonitoringService'] = _MONITORINGSERVICE

# @@protoc_insertion_point(module_scope)

# flake8: noqa
