# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vemmio_client/bsensor.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bvemmio_client/bsensor.proto\x12\x08vemmiopb\":\n\x0fOpenCloseReport\x12\'\n\x05state\x18\x01 \x01(\x0e\x32\x18.vemmiopb.OpenCloseState\"\\\n\x0cMotionReport\x12+\n\x05state\x18\x01 \x01(\x0e\x32\x1c.vemmiopb.MotionReport.State\"\x1f\n\x05State\x12\x08\n\x04IDLE\x10\x00\x12\x0c\n\x08\x44\x45TECTED\x10\x01*H\n\x0eOpenCloseState\x12\x19\n\x15OPEN_CLOSE_STATE_OPEN\x10\x00\x12\x1b\n\x17OPEN_CLOSE_STATE_CLOSED\x10\x01*M\n\x11\x42inarySensorState\x12\x16\n\x12\x42SENSOR_STATE_IDLE\x10\x00\x12 \n\x1c\x42SENSOR_STATE_EVENT_DETECTED\x10\x01\x42=\n-com.vemmio.ha.integration.vemmio.rpc.vemmiopbP\x01Z\n./vemmiopbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vemmio_client.bsensor_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n-com.vemmio.ha.integration.vemmio.rpc.vemmiopbP\001Z\n./vemmiopb'
  _OPENCLOSESTATE._serialized_start=195
  _OPENCLOSESTATE._serialized_end=267
  _BINARYSENSORSTATE._serialized_start=269
  _BINARYSENSORSTATE._serialized_end=346
  _OPENCLOSEREPORT._serialized_start=41
  _OPENCLOSEREPORT._serialized_end=99
  _MOTIONREPORT._serialized_start=101
  _MOTIONREPORT._serialized_end=193
  _MOTIONREPORT_STATE._serialized_start=162
  _MOTIONREPORT_STATE._serialized_end=193
# @@protoc_insertion_point(module_scope)