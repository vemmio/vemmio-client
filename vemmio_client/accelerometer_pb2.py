# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vemmio_client/accelerometer.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from vemmio_client import units_pb2 as vemmio__client_dot_units__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!vemmio_client/accelerometer.proto\x12\x08vemmiopb\x1a\x19vemmio_client/units.proto\"m\n\x13\x41\x63\x63\x65lerometerReport\x12)\n\x04\x61xis\x18\x01 \x01(\x0e\x32\x1b.vemmiopb.AccelerometerAxis\x12\x1c\n\x04unit\x18\x02 \x01(\x0e\x32\x0e.vemmiopb.Unit\x12\r\n\x05value\x18\x03 \x01(\x01*(\n\x11\x41\x63\x63\x65lerometerAxis\x12\x05\n\x01X\x10\x00\x12\x05\n\x01Y\x10\x01\x12\x05\n\x01Z\x10\x02\x42=\n-com.vemmio.ha.integration.vemmio.rpc.vemmiopbP\x01Z\n./vemmiopbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vemmio_client.accelerometer_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n-com.vemmio.ha.integration.vemmio.rpc.vemmiopbP\001Z\n./vemmiopb'
  _ACCELEROMETERAXIS._serialized_start=185
  _ACCELEROMETERAXIS._serialized_end=225
  _ACCELEROMETERREPORT._serialized_start=74
  _ACCELEROMETERREPORT._serialized_end=183
# @@protoc_insertion_point(module_scope)
