# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ydb/public/api/protos/annotations/sensitive.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ydb/public/api/protos/annotations/sensitive.proto',
  package='Ydb',
  syntax='proto3',
  serialized_options=b'\n\016com.yandex.ydb\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n1ydb/public/api/protos/annotations/sensitive.proto\x12\x03Ydb\x1a google/protobuf/descriptor.proto:2\n\tsensitive\x12\x1d.google.protobuf.FieldOptions\x18\xe7\xac\x05 \x01(\x08\x42\x13\n\x0e\x63om.yandex.ydb\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


SENSITIVE_FIELD_NUMBER = 87655
sensitive = _descriptor.FieldDescriptor(
  name='sensitive', full_name='Ydb.sensitive', index=0,
  number=87655, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)

DESCRIPTOR.extensions_by_name['sensitive'] = sensitive
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(sensitive)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
