# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vemmio_client/tamper.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1avemmio_client/tamper.proto\x12\x08vemmiopb\"4\n\x0cTamperReport\x12$\n\x05state\x18\x01 \x01(\x0e\x32\x15.vemmiopb.TamperState*R\n\x0bTamperState\x12\x18\n\x14TAMPER_COVER_REMOVED\x10\x00\x12\x17\n\x13TAMPER_INVALID_CODE\x10\x01\x12\x10\n\x0cTAMPER_MOVED\x10\x02\x42=\n-com.vemmio.ha.integration.vemmio.rpc.vemmiopbP\x01Z\n./vemmiopbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vemmio_client.tamper_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n-com.vemmio.ha.integration.vemmio.rpc.vemmiopbP\001Z\n./vemmiopb'
  _TAMPERSTATE._serialized_start=94
  _TAMPERSTATE._serialized_end=176
  _TAMPERREPORT._serialized_start=40
  _TAMPERREPORT._serialized_end=92
# @@protoc_insertion_point(module_scope)
