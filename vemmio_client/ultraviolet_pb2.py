# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vemmio_client/ultraviolet.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from vemmio_client import metadata_pb2 as vemmio__client_dot_metadata__pb2
from vemmio_client import units_pb2 as vemmio__client_dot_units__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fvemmio_client/ultraviolet.proto\x12\x08vemmiopb\x1a\x1cvemmio_client/metadata.proto\x1a\x19vemmio_client/units.proto\"C\n\x15UltravioletGetRequest\x12*\n\x08metadata\x18\x01 \x01(\x0b\x32\x18.vemmiopb.DeviceMetadata\"E\n\x16UltravioletGetResponse\x12\x1c\n\x04unit\x18\x01 \x01(\x0e\x32\x0e.vemmiopb.Unit\x12\r\n\x05value\x18\x02 \x01(\x01\"@\n\x11UltravioletReport\x12\x1c\n\x04unit\x18\x01 \x01(\x0e\x32\x0e.vemmiopb.Unit\x12\r\n\x05value\x18\x02 \x01(\x01\x32i\n\x12UltravioletService\x12S\n\x0eUltravioletGet\x12\x1f.vemmiopb.UltravioletGetRequest\x1a .vemmiopb.UltravioletGetResponseB=\n-com.vemmio.ha.integration.vemmio.rpc.vemmiopbP\x01Z\n./vemmiopbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vemmio_client.ultraviolet_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n-com.vemmio.ha.integration.vemmio.rpc.vemmiopbP\001Z\n./vemmiopb'
  _ULTRAVIOLETGETREQUEST._serialized_start=102
  _ULTRAVIOLETGETREQUEST._serialized_end=169
  _ULTRAVIOLETGETRESPONSE._serialized_start=171
  _ULTRAVIOLETGETRESPONSE._serialized_end=240
  _ULTRAVIOLETREPORT._serialized_start=242
  _ULTRAVIOLETREPORT._serialized_end=306
  _ULTRAVIOLETSERVICE._serialized_start=308
  _ULTRAVIOLETSERVICE._serialized_end=413
# @@protoc_insertion_point(module_scope)