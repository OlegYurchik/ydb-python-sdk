# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kikimr/public/api/grpc/draft/ydb_clickhouse_internal_v1.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kikimr.public.api.protos import ydb_clickhouse_internal_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__clickhouse__internal__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kikimr/public/api/grpc/draft/ydb_clickhouse_internal_v1.proto',
  package='Ydb.ClickhouseInternal.V1',
  syntax='proto3',
  serialized_pb=_b('\n=kikimr/public/api/grpc/draft/ydb_clickhouse_internal_v1.proto\x12\x19Ydb.ClickhouseInternal.V1\x1a\x36kikimr/public/api/protos/ydb_clickhouse_internal.proto2\xe8\x01\n\x19\x43lickhouseInternalService\x12Q\n\x04Scan\x12#.Ydb.ClickhouseInternal.ScanRequest\x1a$.Ydb.ClickhouseInternal.ScanResponse\x12x\n\x11GetShardLocations\x12\x30.Ydb.ClickhouseInternal.GetShardLocationsRequest\x1a\x31.Ydb.ClickhouseInternal.GetShardLocationsResponseB\x1e\n\x1c\x63om.yandex.ydb.clickhouse.v1b\x06proto3')
  ,
  dependencies=[kikimr_dot_public_dot_api_dot_protos_dot_ydb__clickhouse__internal__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\034com.yandex.ydb.clickhouse.v1'))

_CLICKHOUSEINTERNALSERVICE = _descriptor.ServiceDescriptor(
  name='ClickhouseInternalService',
  full_name='Ydb.ClickhouseInternal.V1.ClickhouseInternalService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=149,
  serialized_end=381,
  methods=[
  _descriptor.MethodDescriptor(
    name='Scan',
    full_name='Ydb.ClickhouseInternal.V1.ClickhouseInternalService.Scan',
    index=0,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__clickhouse__internal__pb2._SCANREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__clickhouse__internal__pb2._SCANRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetShardLocations',
    full_name='Ydb.ClickhouseInternal.V1.ClickhouseInternalService.GetShardLocations',
    index=1,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__clickhouse__internal__pb2._GETSHARDLOCATIONSREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__clickhouse__internal__pb2._GETSHARDLOCATIONSRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLICKHOUSEINTERNALSERVICE)

DESCRIPTOR.services_by_name['ClickhouseInternalService'] = _CLICKHOUSEINTERNALSERVICE

# @@protoc_insertion_point(module_scope)
