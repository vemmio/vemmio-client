# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vemmio_client/thermostat.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from vemmio_client import metadata_pb2 as vemmio__client_dot_metadata__pb2
from vemmio_client import units_pb2 as vemmio__client_dot_units__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1evemmio_client/thermostat.proto\x12\x08vemmiopb\x1a\x1cvemmio_client/metadata.proto\x1a\x19vemmio_client/units.proto\"n\n\x18ThermostatModeSetRequest\x12*\n\x08metadata\x18\x01 \x01(\x0b\x32\x18.vemmiopb.DeviceMetadata\x12&\n\x04mode\x18\x02 \x01(\x0e\x32\x18.vemmiopb.ThermostatMode\"I\n\x1bThermostatModeSupGetRequest\x12*\n\x08metadata\x18\x01 \x01(\x0b\x32\x18.vemmiopb.DeviceMetadata\"G\n\x1cThermostatModeSupGetResponse\x12\'\n\x05modes\x18\x01 \x03(\x0e\x32\x18.vemmiopb.ThermostatMode\"\xaa\x01\n\x1cThermostatSetpointSetRequest\x12*\n\x08metadata\x18\x01 \x01(\x0b\x32\x18.vemmiopb.DeviceMetadata\x12.\n\x04type\x18\x02 \x01(\x0e\x32 .vemmiopb.ThermostatSetpointType\x12.\n\x08setpoint\x18\x03 \x01(\x0b\x32\x1c.vemmiopb.ThermostatSetpoint\"x\n\x1bThermostatFanModeSetRequest\x12*\n\x08metadata\x18\x01 \x01(\x0b\x32\x18.vemmiopb.DeviceMetadata\x12-\n\x08\x66\x61n_mode\x18\x02 \x01(\x0e\x32\x1b.vemmiopb.ThermostatFanMode\"\x14\n\x12ThermostatResponse\">\n\x14ThermostatModeReport\x12&\n\x04mode\x18\x01 \x01(\x0e\x32\x18.vemmiopb.ThermostatMode\"J\n\x18ThermostatSetpointReport\x12.\n\x08setpoint\x18\x01 \x01(\x0b\x32\x1c.vemmiopb.ThermostatSetpoint\"H\n\x17ThermostatFanModeReport\x12-\n\x08\x66\x61n_mode\x18\x01 \x01(\x0e\x32\x1b.vemmiopb.ThermostatFanMode\"\x9f\x01\n\x17ThermostatSetpointRange\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .vemmiopb.ThermostatSetpointType\x12)\n\x03min\x18\x02 \x01(\x0b\x32\x1c.vemmiopb.ThermostatSetpoint\x12)\n\x03max\x18\x03 \x01(\x0b\x32\x1c.vemmiopb.ThermostatSetpoint\"T\n\x12ThermostatSetpoint\x12\r\n\x05value\x18\x01 \x01(\x01\x12\x1c\n\x04unit\x18\x02 \x01(\x0e\x32\x0e.vemmiopb.Unit\x12\x11\n\tprecision\x18\x03 \x01(\r*w\n\x0eThermostatMode\x12\x17\n\x13THERMOSTAT_MODE_OFF\x10\x00\x12\x18\n\x14THERMOSTAT_MODE_HEAT\x10\x01\x12\x18\n\x14THERMOSTAT_MODE_COOL\x10\x02\x12\x18\n\x14THERMOSTAT_MODE_AUTO\x10\x03*\x81\x01\n\x16ThermostatSetpointType\x12!\n\x1dTHERMOSTAT_SETPOINT_TYPE_HEAT\x10\x00\x12!\n\x1dTHERMOSTAT_SETPOINT_TYPE_COOL\x10\x01\x12!\n\x1dTHERMOSTAT_SETPOINT_TYPE_AUTO\x10\x02*\xb0\x01\n\x11ThermostatFanMode\x12\x1b\n\x17THERMOSTAT_FAN_MODE_OFF\x10\x00\x12 \n\x1cTHERMOSTAT_FAN_MODE_AUTO_LOW\x10\x01\x12\x1b\n\x17THERMOSTAT_FAN_MODE_LOW\x10\x02\x12!\n\x1dTHERMOSTAT_FAN_MODE_AUTO_HIGH\x10\x03\x12\x1c\n\x18THERMOSTAT_FAN_MODE_HIGH\x10\x04\x32\x86\x03\n\nThermostat\x12U\n\x11ThermostatModeSet\x12\".vemmiopb.ThermostatModeSetRequest\x1a\x1c.vemmiopb.ThermostatResponse\x12\x65\n\x14ThermostatModeSupGet\x12%.vemmiopb.ThermostatModeSupGetRequest\x1a&.vemmiopb.ThermostatModeSupGetResponse\x12]\n\x15ThermostatSetpointSet\x12&.vemmiopb.ThermostatSetpointSetRequest\x1a\x1c.vemmiopb.ThermostatResponse\x12[\n\x14ThermostatFanModeSet\x12%.vemmiopb.ThermostatFanModeSetRequest\x1a\x1c.vemmiopb.ThermostatResponseB=\n-com.vemmio.ha.integration.vemmio.rpc.vemmiopbP\x01Z\n./vemmiopbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vemmio_client.thermostat_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n-com.vemmio.ha.integration.vemmio.rpc.vemmiopbP\001Z\n./vemmiopb'
  _THERMOSTATMODE._serialized_start=1140
  _THERMOSTATMODE._serialized_end=1259
  _THERMOSTATSETPOINTTYPE._serialized_start=1262
  _THERMOSTATSETPOINTTYPE._serialized_end=1391
  _THERMOSTATFANMODE._serialized_start=1394
  _THERMOSTATFANMODE._serialized_end=1570
  _THERMOSTATMODESETREQUEST._serialized_start=101
  _THERMOSTATMODESETREQUEST._serialized_end=211
  _THERMOSTATMODESUPGETREQUEST._serialized_start=213
  _THERMOSTATMODESUPGETREQUEST._serialized_end=286
  _THERMOSTATMODESUPGETRESPONSE._serialized_start=288
  _THERMOSTATMODESUPGETRESPONSE._serialized_end=359
  _THERMOSTATSETPOINTSETREQUEST._serialized_start=362
  _THERMOSTATSETPOINTSETREQUEST._serialized_end=532
  _THERMOSTATFANMODESETREQUEST._serialized_start=534
  _THERMOSTATFANMODESETREQUEST._serialized_end=654
  _THERMOSTATRESPONSE._serialized_start=656
  _THERMOSTATRESPONSE._serialized_end=676
  _THERMOSTATMODEREPORT._serialized_start=678
  _THERMOSTATMODEREPORT._serialized_end=740
  _THERMOSTATSETPOINTREPORT._serialized_start=742
  _THERMOSTATSETPOINTREPORT._serialized_end=816
  _THERMOSTATFANMODEREPORT._serialized_start=818
  _THERMOSTATFANMODEREPORT._serialized_end=890
  _THERMOSTATSETPOINTRANGE._serialized_start=893
  _THERMOSTATSETPOINTRANGE._serialized_end=1052
  _THERMOSTATSETPOINT._serialized_start=1054
  _THERMOSTATSETPOINT._serialized_end=1138
  _THERMOSTAT._serialized_start=1573
  _THERMOSTAT._serialized_end=1963
# @@protoc_insertion_point(module_scope)
