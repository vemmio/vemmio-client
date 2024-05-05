from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from vemmio_client import accelerometer_pb2 as _accelerometer_pb2
from vemmio_client import battery_pb2 as _battery_pb2
from vemmio_client import bsensor_pb2 as _bsensor_pb2
from vemmio_client import carbon_dioxide_pb2 as _carbon_dioxide_pb2
from vemmio_client import carbon_monoxide_pb2 as _carbon_monoxide_pb2
from vemmio_client import color_pb2 as _color_pb2
from vemmio_client import door_pb2 as _door_pb2
from vemmio_client import doorbell_pb2 as _doorbell_pb2
from vemmio_client import emergency_pb2 as _emergency_pb2
from vemmio_client import firmware_pb2 as _firmware_pb2
from vemmio_client import flood_pb2 as _flood_pb2
from vemmio_client import gate_pb2 as _gate_pb2
from vemmio_client import level_pb2 as _level_pb2
from vemmio_client import lock_pb2 as _lock_pb2
from vemmio_client import metadata_pb2 as _metadata_pb2
from vemmio_client import meter_pb2 as _meter_pb2
from vemmio_client import power_source_pb2 as _power_source_pb2
from vemmio_client import remote_pb2 as _remote_pb2
from vemmio_client import roller_shutter_pb2 as _roller_shutter_pb2
from vemmio_client import seismic_pb2 as _seismic_pb2
from vemmio_client import sensor_pb2 as _sensor_pb2
from vemmio_client import siren_pb2 as _siren_pb2
from vemmio_client import smoke_pb2 as _smoke_pb2
from vemmio_client import status_pb2 as _status_pb2
from vemmio_client import structure_pb2 as _structure_pb2
from vemmio_client import switch_pb2 as _switch_pb2
from vemmio_client import tamper_pb2 as _tamper_pb2
from vemmio_client import taptap_pb2 as _taptap_pb2
from vemmio_client import temperature_pb2 as _temperature_pb2
from vemmio_client import thermostat_pb2 as _thermostat_pb2
from vemmio_client import ultraviolet_pb2 as _ultraviolet_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectivityReport(_message.Message):
    __slots__ = ["state", "timestamp", "uptime"]
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CONNECTED: ConnectivityReport.State
    DISCONNECTED: ConnectivityReport.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPTIME: ConnectivityReport.State
    UPTIME_FIELD_NUMBER: _ClassVar[int]
    state: ConnectivityReport.State
    timestamp: _timestamp_pb2.Timestamp
    uptime: _duration_pb2.Duration
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[ConnectivityReport.State, str]] = ..., uptime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class DeviceReport(_message.Message):
    __slots__ = ["accelerometer", "battery", "carbon_dioxide", "carbon_monoxide_state", "carbon_monoxide_value", "color", "direction", "door", "doorbell", "emergency", "flood", "gas_meter", "gate", "humidity", "illumination", "level", "lock", "metadata", "motion", "open_close", "power_meter", "power_source", "remote", "roller_shutter_level", "seismic_intensity", "seismic_magnitude", "siren", "smoke", "switch", "tamper", "tap_tap", "temperature", "thermostat_fan_mode", "thermostat_mode", "thermostat_setpoint", "timestamp", "tone", "ultraviolet", "volume", "water_meter"]
    ACCELEROMETER_FIELD_NUMBER: _ClassVar[int]
    BATTERY_FIELD_NUMBER: _ClassVar[int]
    CARBON_DIOXIDE_FIELD_NUMBER: _ClassVar[int]
    CARBON_MONOXIDE_STATE_FIELD_NUMBER: _ClassVar[int]
    CARBON_MONOXIDE_VALUE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    DOORBELL_FIELD_NUMBER: _ClassVar[int]
    DOOR_FIELD_NUMBER: _ClassVar[int]
    EMERGENCY_FIELD_NUMBER: _ClassVar[int]
    FLOOD_FIELD_NUMBER: _ClassVar[int]
    GAS_METER_FIELD_NUMBER: _ClassVar[int]
    GATE_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    ILLUMINATION_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    LOCK_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    MOTION_FIELD_NUMBER: _ClassVar[int]
    OPEN_CLOSE_FIELD_NUMBER: _ClassVar[int]
    POWER_METER_FIELD_NUMBER: _ClassVar[int]
    POWER_SOURCE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_FIELD_NUMBER: _ClassVar[int]
    ROLLER_SHUTTER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SEISMIC_INTENSITY_FIELD_NUMBER: _ClassVar[int]
    SEISMIC_MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    SIREN_FIELD_NUMBER: _ClassVar[int]
    SMOKE_FIELD_NUMBER: _ClassVar[int]
    SWITCH_FIELD_NUMBER: _ClassVar[int]
    TAMPER_FIELD_NUMBER: _ClassVar[int]
    TAP_TAP_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    THERMOSTAT_FAN_MODE_FIELD_NUMBER: _ClassVar[int]
    THERMOSTAT_MODE_FIELD_NUMBER: _ClassVar[int]
    THERMOSTAT_SETPOINT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TONE_FIELD_NUMBER: _ClassVar[int]
    ULTRAVIOLET_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    WATER_METER_FIELD_NUMBER: _ClassVar[int]
    accelerometer: _accelerometer_pb2.AccelerometerReport
    battery: _battery_pb2.BatteryReport
    carbon_dioxide: _carbon_dioxide_pb2.CarbonDioxideReport
    carbon_monoxide_state: _carbon_monoxide_pb2.CarbonMonoxideStateReport
    carbon_monoxide_value: _carbon_monoxide_pb2.CarbonMonoxideValueReport
    color: _color_pb2.ColorReport
    direction: _sensor_pb2.DirectionReport
    door: _door_pb2.DoorReport
    doorbell: _doorbell_pb2.DoorbellReport
    emergency: _emergency_pb2.EmergencyReport
    flood: _flood_pb2.FloodReport
    gas_meter: _meter_pb2.MeterReport
    gate: _gate_pb2.GateReport
    humidity: _sensor_pb2.HumidityReport
    illumination: _sensor_pb2.IlluminationReport
    level: _level_pb2.LevelReport
    lock: _lock_pb2.LockReport
    metadata: _metadata_pb2.DeviceMetadata
    motion: _bsensor_pb2.MotionReport
    open_close: _bsensor_pb2.OpenCloseReport
    power_meter: _meter_pb2.MeterReport
    power_source: _power_source_pb2.PowerSourceReport
    remote: _remote_pb2.RemoteReport
    roller_shutter_level: _roller_shutter_pb2.RollerShutterLevelReport
    seismic_intensity: _seismic_pb2.SeismicIntensityReport
    seismic_magnitude: _seismic_pb2.SeismicMagnitudeReport
    siren: _siren_pb2.SirenReport
    smoke: _smoke_pb2.SmokeReport
    switch: _switch_pb2.SwitchReport
    tamper: _tamper_pb2.TamperReport
    tap_tap: _taptap_pb2.TapTapReport
    temperature: _temperature_pb2.TemperatureReport
    thermostat_fan_mode: _thermostat_pb2.ThermostatFanModeReport
    thermostat_mode: _thermostat_pb2.ThermostatModeReport
    thermostat_setpoint: _thermostat_pb2.ThermostatSetpointReport
    timestamp: _timestamp_pb2.Timestamp
    tone: _siren_pb2.ToneReport
    ultraviolet: _ultraviolet_pb2.UltravioletReport
    volume: _siren_pb2.VolumeReport
    water_meter: _meter_pb2.MeterReport
    def __init__(self, metadata: _Optional[_Union[_metadata_pb2.DeviceMetadata, _Mapping]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., switch: _Optional[_Union[_switch_pb2.SwitchReport, _Mapping]] = ..., power_meter: _Optional[_Union[_meter_pb2.MeterReport, _Mapping]] = ..., gas_meter: _Optional[_Union[_meter_pb2.MeterReport, _Mapping]] = ..., water_meter: _Optional[_Union[_meter_pb2.MeterReport, _Mapping]] = ..., open_close: _Optional[_Union[_bsensor_pb2.OpenCloseReport, _Mapping]] = ..., smoke: _Optional[_Union[_smoke_pb2.SmokeReport, _Mapping]] = ..., motion: _Optional[_Union[_bsensor_pb2.MotionReport, _Mapping]] = ..., flood: _Optional[_Union[_flood_pb2.FloodReport, _Mapping]] = ..., carbon_monoxide_state: _Optional[_Union[_carbon_monoxide_pb2.CarbonMonoxideStateReport, _Mapping]] = ..., temperature: _Optional[_Union[_temperature_pb2.TemperatureReport, _Mapping]] = ..., humidity: _Optional[_Union[_sensor_pb2.HumidityReport, _Mapping]] = ..., illumination: _Optional[_Union[_sensor_pb2.IlluminationReport, _Mapping]] = ..., direction: _Optional[_Union[_sensor_pb2.DirectionReport, _Mapping]] = ..., thermostat_mode: _Optional[_Union[_thermostat_pb2.ThermostatModeReport, _Mapping]] = ..., thermostat_setpoint: _Optional[_Union[_thermostat_pb2.ThermostatSetpointReport, _Mapping]] = ..., thermostat_fan_mode: _Optional[_Union[_thermostat_pb2.ThermostatFanModeReport, _Mapping]] = ..., tamper: _Optional[_Union[_tamper_pb2.TamperReport, _Mapping]] = ..., emergency: _Optional[_Union[_emergency_pb2.EmergencyReport, _Mapping]] = ..., door: _Optional[_Union[_door_pb2.DoorReport, _Mapping]] = ..., tap_tap: _Optional[_Union[_taptap_pb2.TapTapReport, _Mapping]] = ..., color: _Optional[_Union[_color_pb2.ColorReport, _Mapping]] = ..., level: _Optional[_Union[_level_pb2.LevelReport, _Mapping]] = ..., battery: _Optional[_Union[_battery_pb2.BatteryReport, _Mapping]] = ..., remote: _Optional[_Union[_remote_pb2.RemoteReport, _Mapping]] = ..., lock: _Optional[_Union[_lock_pb2.LockReport, _Mapping]] = ..., doorbell: _Optional[_Union[_doorbell_pb2.DoorbellReport, _Mapping]] = ..., power_source: _Optional[_Union[_power_source_pb2.PowerSourceReport, _Mapping]] = ..., siren: _Optional[_Union[_siren_pb2.SirenReport, _Mapping]] = ..., tone: _Optional[_Union[_siren_pb2.ToneReport, _Mapping]] = ..., volume: _Optional[_Union[_siren_pb2.VolumeReport, _Mapping]] = ..., accelerometer: _Optional[_Union[_accelerometer_pb2.AccelerometerReport, _Mapping]] = ..., seismic_intensity: _Optional[_Union[_seismic_pb2.SeismicIntensityReport, _Mapping]] = ..., seismic_magnitude: _Optional[_Union[_seismic_pb2.SeismicMagnitudeReport, _Mapping]] = ..., roller_shutter_level: _Optional[_Union[_roller_shutter_pb2.RollerShutterLevelReport, _Mapping]] = ..., carbon_dioxide: _Optional[_Union[_carbon_dioxide_pb2.CarbonDioxideReport, _Mapping]] = ..., carbon_monoxide_value: _Optional[_Union[_carbon_monoxide_pb2.CarbonMonoxideValueReport, _Mapping]] = ..., ultraviolet: _Optional[_Union[_ultraviolet_pb2.UltravioletReport, _Mapping]] = ..., gate: _Optional[_Union[_gate_pb2.GateReport, _Mapping]] = ...) -> None: ...

class GatewayReport(_message.Message):
    __slots__ = ["connectivity", "device", "firmware_update_status", "mac", "status_check", "structure"]
    CONNECTIVITY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_UPDATE_STATUS_FIELD_NUMBER: _ClassVar[int]
    MAC_FIELD_NUMBER: _ClassVar[int]
    STATUS_CHECK_FIELD_NUMBER: _ClassVar[int]
    STRUCTURE_FIELD_NUMBER: _ClassVar[int]
    connectivity: ConnectivityReport
    device: DeviceReport
    firmware_update_status: _firmware_pb2.FirmwareUpdateStatusReport
    mac: str
    status_check: _status_pb2.StatusCheckReport
    structure: _structure_pb2.StructureReport
    def __init__(self, mac: _Optional[str] = ..., connectivity: _Optional[_Union[ConnectivityReport, _Mapping]] = ..., device: _Optional[_Union[DeviceReport, _Mapping]] = ..., status_check: _Optional[_Union[_status_pb2.StatusCheckReport, _Mapping]] = ..., firmware_update_status: _Optional[_Union[_firmware_pb2.FirmwareUpdateStatusReport, _Mapping]] = ..., structure: _Optional[_Union[_structure_pb2.StructureReport, _Mapping]] = ...) -> None: ...

class ReportRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
