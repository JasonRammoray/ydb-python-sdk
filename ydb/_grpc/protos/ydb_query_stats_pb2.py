# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/ydb_query_stats.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/ydb_query_stats.proto',
  package='Ydb.TableStats',
  syntax='proto3',
  serialized_options=b'\n\010tech.ydbZ=github.com/ydb-platform/ydb-go-genproto/protos/Ydb_TableStats\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1cprotos/ydb_query_stats.proto\x12\x0eYdb.TableStats\"-\n\x0eOperationStats\x12\x0c\n\x04rows\x18\x01 \x01(\x04\x12\r\n\x05\x62ytes\x18\x02 \x01(\x04\"\xd1\x01\n\x10TableAccessStats\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\x05reads\x18\x03 \x01(\x0b\x32\x1e.Ydb.TableStats.OperationStats\x12/\n\x07updates\x18\x04 \x01(\x0b\x32\x1e.Ydb.TableStats.OperationStats\x12/\n\x07\x64\x65letes\x18\x05 \x01(\x0b\x32\x1e.Ydb.TableStats.OperationStats\x12\x18\n\x10partitions_count\x18\x06 \x01(\x04J\x04\x08\x02\x10\x03\"\xa3\x01\n\x0fQueryPhaseStats\x12\x13\n\x0b\x64uration_us\x18\x01 \x01(\x04\x12\x36\n\x0ctable_access\x18\x02 \x03(\x0b\x32 .Ydb.TableStats.TableAccessStats\x12\x13\n\x0b\x63pu_time_us\x18\x03 \x01(\x04\x12\x17\n\x0f\x61\x66\x66\x65\x63ted_shards\x18\x04 \x01(\x04\x12\x15\n\rliteral_phase\x18\x05 \x01(\x08\"P\n\x10\x43ompilationStats\x12\x12\n\nfrom_cache\x18\x01 \x01(\x08\x12\x13\n\x0b\x64uration_us\x18\x02 \x01(\x04\x12\x13\n\x0b\x63pu_time_us\x18\x03 \x01(\x04\"\xf4\x01\n\nQueryStats\x12\x35\n\x0cquery_phases\x18\x01 \x03(\x0b\x32\x1f.Ydb.TableStats.QueryPhaseStats\x12\x35\n\x0b\x63ompilation\x18\x02 \x01(\x0b\x32 .Ydb.TableStats.CompilationStats\x12\x1b\n\x13process_cpu_time_us\x18\x03 \x01(\x04\x12\x12\n\nquery_plan\x18\x04 \x01(\t\x12\x11\n\tquery_ast\x18\x05 \x01(\t\x12\x19\n\x11total_duration_us\x18\x06 \x01(\x04\x12\x19\n\x11total_cpu_time_us\x18\x07 \x01(\x04\x42L\n\x08tech.ydbZ=github.com/ydb-platform/ydb-go-genproto/protos/Ydb_TableStats\xf8\x01\x01\x62\x06proto3'
)




_OPERATIONSTATS = _descriptor.Descriptor(
  name='OperationStats',
  full_name='Ydb.TableStats.OperationStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rows', full_name='Ydb.TableStats.OperationStats.rows', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bytes', full_name='Ydb.TableStats.OperationStats.bytes', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=93,
)


_TABLEACCESSSTATS = _descriptor.Descriptor(
  name='TableAccessStats',
  full_name='Ydb.TableStats.TableAccessStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Ydb.TableStats.TableAccessStats.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reads', full_name='Ydb.TableStats.TableAccessStats.reads', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updates', full_name='Ydb.TableStats.TableAccessStats.updates', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deletes', full_name='Ydb.TableStats.TableAccessStats.deletes', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='partitions_count', full_name='Ydb.TableStats.TableAccessStats.partitions_count', index=4,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=305,
)


_QUERYPHASESTATS = _descriptor.Descriptor(
  name='QueryPhaseStats',
  full_name='Ydb.TableStats.QueryPhaseStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='duration_us', full_name='Ydb.TableStats.QueryPhaseStats.duration_us', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='table_access', full_name='Ydb.TableStats.QueryPhaseStats.table_access', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cpu_time_us', full_name='Ydb.TableStats.QueryPhaseStats.cpu_time_us', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='affected_shards', full_name='Ydb.TableStats.QueryPhaseStats.affected_shards', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='literal_phase', full_name='Ydb.TableStats.QueryPhaseStats.literal_phase', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=308,
  serialized_end=471,
)


_COMPILATIONSTATS = _descriptor.Descriptor(
  name='CompilationStats',
  full_name='Ydb.TableStats.CompilationStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_cache', full_name='Ydb.TableStats.CompilationStats.from_cache', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duration_us', full_name='Ydb.TableStats.CompilationStats.duration_us', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cpu_time_us', full_name='Ydb.TableStats.CompilationStats.cpu_time_us', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=473,
  serialized_end=553,
)


_QUERYSTATS = _descriptor.Descriptor(
  name='QueryStats',
  full_name='Ydb.TableStats.QueryStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query_phases', full_name='Ydb.TableStats.QueryStats.query_phases', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compilation', full_name='Ydb.TableStats.QueryStats.compilation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='process_cpu_time_us', full_name='Ydb.TableStats.QueryStats.process_cpu_time_us', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query_plan', full_name='Ydb.TableStats.QueryStats.query_plan', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query_ast', full_name='Ydb.TableStats.QueryStats.query_ast', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_duration_us', full_name='Ydb.TableStats.QueryStats.total_duration_us', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_cpu_time_us', full_name='Ydb.TableStats.QueryStats.total_cpu_time_us', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=556,
  serialized_end=800,
)

_TABLEACCESSSTATS.fields_by_name['reads'].message_type = _OPERATIONSTATS
_TABLEACCESSSTATS.fields_by_name['updates'].message_type = _OPERATIONSTATS
_TABLEACCESSSTATS.fields_by_name['deletes'].message_type = _OPERATIONSTATS
_QUERYPHASESTATS.fields_by_name['table_access'].message_type = _TABLEACCESSSTATS
_QUERYSTATS.fields_by_name['query_phases'].message_type = _QUERYPHASESTATS
_QUERYSTATS.fields_by_name['compilation'].message_type = _COMPILATIONSTATS
DESCRIPTOR.message_types_by_name['OperationStats'] = _OPERATIONSTATS
DESCRIPTOR.message_types_by_name['TableAccessStats'] = _TABLEACCESSSTATS
DESCRIPTOR.message_types_by_name['QueryPhaseStats'] = _QUERYPHASESTATS
DESCRIPTOR.message_types_by_name['CompilationStats'] = _COMPILATIONSTATS
DESCRIPTOR.message_types_by_name['QueryStats'] = _QUERYSTATS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OperationStats = _reflection.GeneratedProtocolMessageType('OperationStats', (_message.Message,), {
  'DESCRIPTOR' : _OPERATIONSTATS,
  '__module__' : 'protos.ydb_query_stats_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.TableStats.OperationStats)
  })
_sym_db.RegisterMessage(OperationStats)

TableAccessStats = _reflection.GeneratedProtocolMessageType('TableAccessStats', (_message.Message,), {
  'DESCRIPTOR' : _TABLEACCESSSTATS,
  '__module__' : 'protos.ydb_query_stats_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.TableStats.TableAccessStats)
  })
_sym_db.RegisterMessage(TableAccessStats)

QueryPhaseStats = _reflection.GeneratedProtocolMessageType('QueryPhaseStats', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPHASESTATS,
  '__module__' : 'protos.ydb_query_stats_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.TableStats.QueryPhaseStats)
  })
_sym_db.RegisterMessage(QueryPhaseStats)

CompilationStats = _reflection.GeneratedProtocolMessageType('CompilationStats', (_message.Message,), {
  'DESCRIPTOR' : _COMPILATIONSTATS,
  '__module__' : 'protos.ydb_query_stats_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.TableStats.CompilationStats)
  })
_sym_db.RegisterMessage(CompilationStats)

QueryStats = _reflection.GeneratedProtocolMessageType('QueryStats', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSTATS,
  '__module__' : 'protos.ydb_query_stats_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.TableStats.QueryStats)
  })
_sym_db.RegisterMessage(QueryStats)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

# flake8: noqa
