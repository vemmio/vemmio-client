# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vemmio_client/structure.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dvemmio_client/structure.proto\x12\x08vemmiopb\"\x12\n\x10StructureRequest\"A\n\x11StructureResponse\x12,\n\tstructure\x18\x01 \x01(\x0b\x32\x19.vemmiopb.StructureReport\"f\n\x0fStructureReport\x12\x0b\n\x03mac\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x10\n\x08revision\x18\x03 \x01(\t\x12&\n\x05nodes\x18\x04 \x03(\x0b\x32\x17.vemmiopb.StructureNode\"3\n\rStructureNode\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\x12\x14\n\x0c\x63\x61pabilities\x18\x02 \x03(\t2[\n\x10StructureService\x12G\n\x0cGetStructure\x12\x1a.vemmiopb.StructureRequest\x1a\x1b.vemmiopb.StructureResponseB=\n-com.vemmio.ha.integration.vemmio.rpc.vemmiopbP\x01Z\n./vemmiopbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vemmio_client.structure_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n-com.vemmio.ha.integration.vemmio.rpc.vemmiopbP\001Z\n./vemmiopb'
  _STRUCTUREREQUEST._serialized_start=43
  _STRUCTUREREQUEST._serialized_end=61
  _STRUCTURERESPONSE._serialized_start=63
  _STRUCTURERESPONSE._serialized_end=128
  _STRUCTUREREPORT._serialized_start=130
  _STRUCTUREREPORT._serialized_end=232
  _STRUCTURENODE._serialized_start=234
  _STRUCTURENODE._serialized_end=285
  _STRUCTURESERVICE._serialized_start=287
  _STRUCTURESERVICE._serialized_end=378
# @@protoc_insertion_point(module_scope)
