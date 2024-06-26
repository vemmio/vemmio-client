# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vemmio_client/devices.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from vemmio_client import accelerometer_pb2 as vemmio__client_dot_accelerometer__pb2
from vemmio_client import color_pb2 as vemmio__client_dot_color__pb2
from vemmio_client import metadata_pb2 as vemmio__client_dot_metadata__pb2
from vemmio_client import power_source_pb2 as vemmio__client_dot_power__source__pb2
from vemmio_client import thermostat_pb2 as vemmio__client_dot_thermostat__pb2
from vemmio_client import units_pb2 as vemmio__client_dot_units__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bvemmio_client/devices.proto\x12\x08vemmiopb\x1a!vemmio_client/accelerometer.proto\x1a\x19vemmio_client/color.proto\x1a\x1cvemmio_client/metadata.proto\x1a vemmio_client/power_source.proto\x1a\x1evemmio_client/thermostat.proto\x1a\x19vemmio_client/units.proto\"\x14\n\x12\x44\x65vicesListRequest\"8\n\x13\x44\x65vicesListResponse\x12!\n\x07\x64\x65vices\x18\x01 \x03(\x0b\x32\x10.vemmiopb.Device\"\xbf\x02\n\x06\x44\x65vice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12*\n\x08metadata\x18\x02 \x01(\x0b\x32\x18.vemmiopb.DeviceMetadata\x12*\n\x0c\x63\x61pabilities\x18\x03 \x03(\x0b\x32\x14.vemmiopb.Capability\x12\x0c\n\x04i18n\x18\x04 \x01(\t\x12%\n\x05group\x18\x05 \x01(\x0e\x32\x16.vemmiopb.Device.Group\"\x99\x01\n\x05Group\x12\t\n\x05OTHER\x10\x00\x12\x0b\n\x07\x43LIMATE\x10\x01\x12\x0c\n\x08SECURITY\x10\x02\x12\t\n\x05POWER\x10\x03\x12\x13\n\x0fROLLER_SHUTTERS\x10\x04\x12\x0b\n\x07\x43\x41MERAS\x10\x05\x12\r\n\tDOORBELLS\x10\x06\x12\x0c\n\x08GATEWAYS\x10\x07\x12\n\n\x06LIGHTS\x10\x08\x12\t\n\x05GATES\x10\t\x12\t\n\x05SOUND\x10\n\"\xf5\r\n\nCapability\x12,\n\x06switch\x18\x01 \x01(\x0b\x32\x1a.vemmiopb.SwitchCapabilityH\x00\x12\x30\n\x0bpower_meter\x18\x02 \x01(\x0b\x32\x19.vemmiopb.MeterCapabilityH\x00\x12.\n\tgas_meter\x18\x03 \x01(\x0b\x32\x19.vemmiopb.MeterCapabilityH\x00\x12\x30\n\x0bwater_meter\x18\x04 \x01(\x0b\x32\x19.vemmiopb.MeterCapabilityH\x00\x12\x33\n\nopen_close\x18\x05 \x01(\x0b\x32\x1d.vemmiopb.OpenCloseCapabilityH\x00\x12;\n\x0esmoke_detector\x18\x06 \x01(\x0b\x32!.vemmiopb.SmokeDetectorCapabilityH\x00\x12=\n\x0fmotion_detector\x18\x07 \x01(\x0b\x32\".vemmiopb.MotionDetectorCapabilityH\x00\x12;\n\x0e\x66lood_detector\x18\x08 \x01(\x0b\x32!.vemmiopb.FloodDetectorCapabilityH\x00\x12N\n\x18\x63\x61rbon_monoxide_detector\x18\t \x01(\x0b\x32*.vemmiopb.CarbonMonoxideDetectorCapabilityH\x00\x12\x34\n\nthermostat\x18\n \x01(\x0b\x32\x1e.vemmiopb.ThermostatCapabilityH\x00\x12\x36\n\x0btemperature\x18\x0b \x01(\x0b\x32\x1f.vemmiopb.TemperatureCapabilityH\x00\x12\x30\n\x08humidity\x18\x0c \x01(\x0b\x32\x1c.vemmiopb.HumidityCapabilityH\x00\x12\x38\n\x0cillumination\x18\r \x01(\x0b\x32 .vemmiopb.IlluminationCapabilityH\x00\x12\x32\n\tdirection\x18\x0e \x01(\x0b\x32\x1d.vemmiopb.DirectionCapabilityH\x00\x12,\n\x06tamper\x18\x0f \x01(\x0b\x32\x1a.vemmiopb.TamperCapabilityH\x00\x12\x32\n\temergency\x18\x10 \x01(\x0b\x32\x1d.vemmiopb.EmergencyCapabilityH\x00\x12(\n\x04\x64oor\x18\x11 \x01(\x0b\x32\x18.vemmiopb.DoorCapabilityH\x00\x12-\n\x07tap_tap\x18\x12 \x01(\x0b\x32\x1a.vemmiopb.TapTapCapabilityH\x00\x12*\n\x05\x63olor\x18\x13 \x01(\x0b\x32\x19.vemmiopb.ColorCapabilityH\x00\x12*\n\x05level\x18\x14 \x01(\x0b\x32\x19.vemmiopb.LevelCapabilityH\x00\x12.\n\x07\x62\x61ttery\x18\x15 \x01(\x0b\x32\x1b.vemmiopb.BatteryCapabilityH\x00\x12(\n\x04lock\x18\x16 \x01(\x0b\x32\x18.vemmiopb.LockCapabilityH\x00\x12,\n\x06remote\x18\x17 \x01(\x0b\x32\x1a.vemmiopb.RemoteCapabilityH\x00\x12\x37\n\x0cpower_source\x18\x18 \x01(\x0b\x32\x1f.vemmiopb.PowerSourceCapabilityH\x00\x12;\n\x0eroller_shutter\x18\x19 \x01(\x0b\x32!.vemmiopb.RollerShutterCapabilityH\x00\x12:\n\rconfiguration\x18\x1a \x01(\x0b\x32!.vemmiopb.ConfigurationCapabilityH\x00\x12\x30\n\x08\x64oorbell\x18\x1b \x01(\x0b\x32\x1c.vemmiopb.DoorbellCapabilityH\x00\x12*\n\x05siren\x18\x1c \x01(\x0b\x32\x19.vemmiopb.SirenCapabilityH\x00\x12:\n\raccelerometer\x18\x1d \x01(\x0b\x32!.vemmiopb.AccelerometerCapabilityH\x00\x12.\n\x07seismic\x18\x1e \x01(\x0b\x32\x1b.vemmiopb.SeismicCapabilityH\x00\x12L\n\x17\x63\x61rbon_dioxide_detector\x18\x1f \x01(\x0b\x32).vemmiopb.CarbonDioxideDetectorCapabilityH\x00\x12.\n\x07voltage\x18  \x01(\x0b\x32\x1b.vemmiopb.VoltageCapabilityH\x00\x12\x36\n\x0bultraviolet\x18! \x01(\x0b\x32\x1f.vemmiopb.UltravioletCapabilityH\x00\x42\x0c\n\ncapability\"\x12\n\x10SwitchCapability\"?\n\x0fMeterCapability\x12\x1d\n\x05units\x18\x01 \x03(\x0e\x32\x0e.vemmiopb.Unit\x12\r\n\x05reset\x18\x02 \x01(\x08\"\x15\n\x13OpenCloseCapability\"\x19\n\x17SmokeDetectorCapability\"\x1a\n\x18MotionDetectorCapability\"\x19\n\x17\x46loodDetectorCapability\"A\n CarbonMonoxideDetectorCapability\x12\x1d\n\x05units\x18\x01 \x03(\x0e\x32\x0e.vemmiopb.Unit\"!\n\x1f\x43\x61rbonDioxideDetectorCapability\"I\n\x14ThermostatCapability\x12\x31\n\x06ranges\x18\x01 \x03(\x0b\x32!.vemmiopb.ThermostatSetpointRange\"6\n\x15TemperatureCapability\x12\x1d\n\x05units\x18\x01 \x03(\x0e\x32\x0e.vemmiopb.Unit\"3\n\x12HumidityCapability\x12\x1d\n\x05units\x18\x01 \x03(\x0e\x32\x0e.vemmiopb.Unit\"7\n\x16IlluminationCapability\x12\x1d\n\x05units\x18\x01 \x03(\x0e\x32\x0e.vemmiopb.Unit\"4\n\x13\x44irectionCapability\x12\x1d\n\x05units\x18\x01 \x03(\x0e\x32\x0e.vemmiopb.Unit\"\x12\n\x10TamperCapability\"\x15\n\x13\x45mergencyCapability\"\x10\n\x0e\x44oorCapability\"\x12\n\x10TapTapCapability\"?\n\x0f\x43olorCapability\x12,\n\ncomponents\x18\x01 \x03(\x0e\x32\x18.vemmiopb.ColorComponent\"\x11\n\x0fLevelCapability\"\x13\n\x11\x42\x61tteryCapability\"\x10\n\x0eLockCapability\"\x12\n\x10RemoteCapability\"C\n\x15PowerSourceCapability\x12*\n\x06\x65vents\x18\x01 \x03(\x0e\x32\x1a.vemmiopb.PowerSourceEvent\"\x19\n\x17RollerShutterCapability\"\x19\n\x17\x43onfigurationCapability\"\x14\n\x12\x44oorbellCapability\"\x11\n\x0fSirenCapability\"\xa1\x01\n\x17\x41\x63\x63\x65lerometerCapability\x12\x34\n\x04\x61xes\x18\x01 \x03(\x0b\x32&.vemmiopb.AccelerometerCapability.Axis\x1aP\n\x04\x41xis\x12)\n\x04\x61xis\x18\x01 \x01(\x0e\x32\x1b.vemmiopb.AccelerometerAxis\x12\x1d\n\x05units\x18\x02 \x03(\x0e\x32\x0e.vemmiopb.Unit\"Y\n\x11SeismicCapability\x12!\n\tintensity\x18\x01 \x03(\x0e\x32\x0e.vemmiopb.Unit\x12!\n\tmagnitude\x18\x02 \x03(\x0e\x32\x0e.vemmiopb.Unit\"2\n\x11VoltageCapability\x12\x1d\n\x05units\x18\x01 \x03(\x0e\x32\x0e.vemmiopb.Unit\"6\n\x15UltravioletCapability\x12\x1d\n\x05units\x18\x01 \x03(\x0e\x32\x0e.vemmiopb.Unit2U\n\x07\x44\x65vices\x12J\n\x0b\x44\x65vicesList\x12\x1c.vemmiopb.DevicesListRequest\x1a\x1d.vemmiopb.DevicesListResponseB=\n-com.vemmio.ha.integration.vemmio.rpc.vemmiopbP\x01Z\n./vemmiopbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vemmio_client.devices_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n-com.vemmio.ha.integration.vemmio.rpc.vemmiopbP\001Z\n./vemmiopb'
  _DEVICESLISTREQUEST._serialized_start=226
  _DEVICESLISTREQUEST._serialized_end=246
  _DEVICESLISTRESPONSE._serialized_start=248
  _DEVICESLISTRESPONSE._serialized_end=304
  _DEVICE._serialized_start=307
  _DEVICE._serialized_end=626
  _DEVICE_GROUP._serialized_start=473
  _DEVICE_GROUP._serialized_end=626
  _CAPABILITY._serialized_start=629
  _CAPABILITY._serialized_end=2410
  _SWITCHCAPABILITY._serialized_start=2412
  _SWITCHCAPABILITY._serialized_end=2430
  _METERCAPABILITY._serialized_start=2432
  _METERCAPABILITY._serialized_end=2495
  _OPENCLOSECAPABILITY._serialized_start=2497
  _OPENCLOSECAPABILITY._serialized_end=2518
  _SMOKEDETECTORCAPABILITY._serialized_start=2520
  _SMOKEDETECTORCAPABILITY._serialized_end=2545
  _MOTIONDETECTORCAPABILITY._serialized_start=2547
  _MOTIONDETECTORCAPABILITY._serialized_end=2573
  _FLOODDETECTORCAPABILITY._serialized_start=2575
  _FLOODDETECTORCAPABILITY._serialized_end=2600
  _CARBONMONOXIDEDETECTORCAPABILITY._serialized_start=2602
  _CARBONMONOXIDEDETECTORCAPABILITY._serialized_end=2667
  _CARBONDIOXIDEDETECTORCAPABILITY._serialized_start=2669
  _CARBONDIOXIDEDETECTORCAPABILITY._serialized_end=2702
  _THERMOSTATCAPABILITY._serialized_start=2704
  _THERMOSTATCAPABILITY._serialized_end=2777
  _TEMPERATURECAPABILITY._serialized_start=2779
  _TEMPERATURECAPABILITY._serialized_end=2833
  _HUMIDITYCAPABILITY._serialized_start=2835
  _HUMIDITYCAPABILITY._serialized_end=2886
  _ILLUMINATIONCAPABILITY._serialized_start=2888
  _ILLUMINATIONCAPABILITY._serialized_end=2943
  _DIRECTIONCAPABILITY._serialized_start=2945
  _DIRECTIONCAPABILITY._serialized_end=2997
  _TAMPERCAPABILITY._serialized_start=2999
  _TAMPERCAPABILITY._serialized_end=3017
  _EMERGENCYCAPABILITY._serialized_start=3019
  _EMERGENCYCAPABILITY._serialized_end=3040
  _DOORCAPABILITY._serialized_start=3042
  _DOORCAPABILITY._serialized_end=3058
  _TAPTAPCAPABILITY._serialized_start=3060
  _TAPTAPCAPABILITY._serialized_end=3078
  _COLORCAPABILITY._serialized_start=3080
  _COLORCAPABILITY._serialized_end=3143
  _LEVELCAPABILITY._serialized_start=3145
  _LEVELCAPABILITY._serialized_end=3162
  _BATTERYCAPABILITY._serialized_start=3164
  _BATTERYCAPABILITY._serialized_end=3183
  _LOCKCAPABILITY._serialized_start=3185
  _LOCKCAPABILITY._serialized_end=3201
  _REMOTECAPABILITY._serialized_start=3203
  _REMOTECAPABILITY._serialized_end=3221
  _POWERSOURCECAPABILITY._serialized_start=3223
  _POWERSOURCECAPABILITY._serialized_end=3290
  _ROLLERSHUTTERCAPABILITY._serialized_start=3292
  _ROLLERSHUTTERCAPABILITY._serialized_end=3317
  _CONFIGURATIONCAPABILITY._serialized_start=3319
  _CONFIGURATIONCAPABILITY._serialized_end=3344
  _DOORBELLCAPABILITY._serialized_start=3346
  _DOORBELLCAPABILITY._serialized_end=3366
  _SIRENCAPABILITY._serialized_start=3368
  _SIRENCAPABILITY._serialized_end=3385
  _ACCELEROMETERCAPABILITY._serialized_start=3388
  _ACCELEROMETERCAPABILITY._serialized_end=3549
  _ACCELEROMETERCAPABILITY_AXIS._serialized_start=3469
  _ACCELEROMETERCAPABILITY_AXIS._serialized_end=3549
  _SEISMICCAPABILITY._serialized_start=3551
  _SEISMICCAPABILITY._serialized_end=3640
  _VOLTAGECAPABILITY._serialized_start=3642
  _VOLTAGECAPABILITY._serialized_end=3692
  _ULTRAVIOLETCAPABILITY._serialized_start=3694
  _ULTRAVIOLETCAPABILITY._serialized_end=3748
  _DEVICES._serialized_start=3750
  _DEVICES._serialized_end=3835
# @@protoc_insertion_point(module_scope)
