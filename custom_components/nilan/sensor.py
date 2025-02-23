"""Platform for sensor integration."""

from __future__ import annotations

from collections import namedtuple

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import (
    CONCENTRATION_PARTS_PER_MILLION,
    PERCENTAGE,
    UnitOfTemperature,
    UnitOfTime,
)
from homeassistant.helpers.entity import EntityCategory

from .__init__ import NilanEntity
from .const import DOMAIN

Map = namedtuple(
    "map", "name default_unit device_class state_class entity_category icon enabled"
)

ATTRIBUTE_TO_SENSORS = {
    "get_t0_controller_temperature": [
        Map(
            "controller_board_temperature_t0",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            EntityCategory.DIAGNOSTIC,
            None,
            True,
        )
    ],
    "get_t1_intake_temperature": [
        Map(
            "fresh_air_intake_temperature_t1",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_t2_inlet_temperature": [
        Map(
            "supply_air_temperature_t2",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_t3_exhaust_temperature": [
        Map(
            "return_air_temperature_t3",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_t4_outlet": [
        Map(
            "waste_air_temperature_t4",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_t5_condenser_temperature": [
        Map(
            "condenser_temperature_t5",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            EntityCategory.DIAGNOSTIC,
            None,
            True,
        )
    ],
    "get_t6_evaporator_temperature": [
        Map(
            "waste_air_temperature_t6",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_t7_inlet_temperature_after_heater": [
        Map(
            "supply_air_temperature_t7",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_t8_outdoor_temperature": [
        Map(
            "fresh_air_intake_temperature_t8",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_t10_external_temperature": [
        Map(
            "return_air_temperature_t10",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_t13_return_temperature": [
        Map(
            "return_water_temperature_t13",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_t14_supply_temperature": [
        Map(
            "supply_water_temperature_t14",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_t15_user_panel_temperature": [
        Map(
            "user_panel_temperature_t15",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            EntityCategory.DIAGNOSTIC,
            None,
            True,
        )
    ],
    "get_t16_sacrificial_anode_temperature": [
        Map(
            "anode_temperature_t16",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_central_heating_setpoint": [
        Map(
            "central_heating_setpoint",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_humidity": [
        Map(
            "humidity",
            PERCENTAGE,
            SensorDeviceClass.HUMIDITY,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_average_humidity": [
        Map(
            "24h_average_humidity",
            PERCENTAGE,
            SensorDeviceClass.HUMIDITY,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_after_heating_element_capacity": [
        Map(
            "after_heating_element_capacity",
            PERCENTAGE,
            None,
            SensorStateClass.MEASUREMENT,
            None,
            "mdi:radiator",
            True,
        )
    ],
    "get_co2_sensor_value": [
        Map(
            "co2_sensor",
            CONCENTRATION_PARTS_PER_MILLION,
            SensorDeviceClass.CO2,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_control_state": [
        Map(
            "control_state",
            None,
            None,
            None,
            None,
            "mdi:state-machine",
            True,
        )
    ],
    "get_after_heating_type": [
        Map(
            "after_heating_type",
            None,
            None,
            None,
            EntityCategory.DIAGNOSTIC,
            None,
            True,
        )
    ],
    "get_time_in_control_state": [
        Map(
            "time_in_control_state",
            None,
            None,
            None,
            None,
            "mdi:calendar-clock",
            True,
        )
    ],
    "get_alarm_count": [
        Map(
            "alarms_active",
            None,
            None,
            SensorStateClass.MEASUREMENT,
            None,
            "mdi:alert-circle-outline",
            True,
        )
    ],
    "get_days_since_air_filter_change": [
        Map(
            "days_since_air_filter_change",
            UnitOfTime.DAYS,
            None,
            SensorStateClass.MEASUREMENT,
            None,
            "mdi:calendar-start",
            True,
        )
    ],
    "get_days_to_air_filter_change": [
        Map(
            "days_to_air_filter_change",
            UnitOfTime.DAYS,
            None,
            SensorStateClass.MEASUREMENT,
            None,
            "mdi:calendar-end",
            True,
        )
    ],
    "get_summer_state": [
        Map(
            "climate_season",
            None,
            None,
            None,
            None,
            "mdi:sun-snowflake",
            True,
        )
    ],
    "get_exchanger_efficiency": [
        Map(
            "exchanger_efficiency",
            PERCENTAGE,
            None,
            SensorStateClass.MEASUREMENT,
            None,
            "mdi:air-filter",
            True,
        )
    ],
    "get_time": [
        Map(
            "time",
            None,
            None,
            None,
            None,
            "mdi:calendar-clock",
            True,
        )
    ],
    "get_ventilation_state": [
        Map(
            "ventilation_state",
            None,
            None,
            None,
            None,
            "mdi:state-machine",
            True,
        )
    ],
    "get_anode_state": [
        Map(
            "anode_state",
            None,
            None,
            None,
            None,
            None,
            True,
        )
    ],
    "get_supply_fan_level": [
        Map(
            "supply_fan_level",
            None,
            None,
            SensorStateClass.MEASUREMENT,
            None,
            "mdi:fan",
            True,
        )
    ],
    "get_return_fan_level": [
        Map(
            "return_fan_level",
            None,
            None,
            SensorStateClass.MEASUREMENT,
            None,
            "mdi:fan",
            True,
        )
    ],
    "get_return_fan_speed": [
        Map(
            "return_fan_speed",
            PERCENTAGE,
            None,
            SensorStateClass.MEASUREMENT,
            None,
            "mdi:fan",
            True,
        )
    ],
    "get_supply_fan_speed": [
        Map(
            "supply_fan_speed",
            PERCENTAGE,
            None,
            SensorStateClass.MEASUREMENT,
            None,
            "mdi:fan",
            True,
        )
    ],
    "get_display_text_1": [
        Map(
            "display_text_line_1",
            None,
            None,
            None,
            None,
            None,
            True,
        )
    ],
    "get_display_text_2": [
        Map(
            "display_text_line_2",
            None,
            None,
            None,
            None,
            None,
            True,
        )
    ],
    "get_bus_version": [
        Map(
            "modbus_version",
            None,
            None,
            SensorStateClass.MEASUREMENT,
            EntityCategory.DIAGNOSTIC,
            None,
            True,
        )
    ],
    "get_hps_compressor_capacity": [
        Map(
            "hps_compressor_capacity",
            PERCENTAGE,
            None,
            SensorStateClass.MEASUREMENT,
            None,
            "mdi:air-filter",
            True,
        )
    ],
    "get_hps_heat_pump_state": [
        Map(
            "hps_heat_pump_state",
            None,
            None,
            None,
            None,
            "mdi:state-machine",
            True,
        )
    ],
    "get_hps_t16_return_temperature": [
        Map(
            "hps_t16_return_temperature",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_hps_t17_supply_temperature": [
        Map(
            "hps_t17_supply_temperature",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_hps_t18_tank_temperature": [
        Map(
            "hps_t18_tank_temperature",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_hps_t20_ambient_temperature": [
        Map(
            "hps_t20_ambient_temperature",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_hps_t21_shw_top_temperature": [
        Map(
            "hps_t21_shw_top_temperature",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_hps_t22_shw_bottom_temperature": [
        Map(
            "hps_t22_shw_bottom_temperature",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_hps_t35_pressure_pipe_temperature": [
        Map(
            "hps_t35_pressure_pipe_temperature",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_hps_output_compvolt1": [
        Map(
            "hps_output_compvolt1",
            None,
            SensorDeviceClass.VOLTAGE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_hps_alarm_count": [
        Map(
            "hps_alarms_active",
            None,
            None,
            SensorStateClass.MEASUREMENT,
            None,
            "mdi:alert-circle-outline",
            True,
        )
    ],
    "get_hps_hot_water_setpoint_actual": [
        Map(
            "hps_hot_water_setpoint_actual",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
    "get_hps_heating_setpoint_actual": [
        Map(
            "hps_heating_setpoint_actual",
            UnitOfTemperature.CELSIUS,
            SensorDeviceClass.TEMPERATURE,
            SensorStateClass.MEASUREMENT,
            None,
            None,
            True,
        )
    ],
}


async def async_setup_entry(HomeAssistant, config_entry, async_add_entities):
    """Set up the sensor platform."""
    device = HomeAssistant.data[DOMAIN][config_entry.entry_id]
    sensors = []
    for attribute in device.get_assigned("sensor"):
        if attribute in ATTRIBUTE_TO_SENSORS:
            maps = ATTRIBUTE_TO_SENSORS[attribute]
            sensors.extend(
                [
                    NilanCTS602Sensor(
                        device,
                        attribute,
                        m.name,
                        m.default_unit,
                        m.device_class,
                        m.state_class,
                        m.entity_category,
                        m.icon,
                        m.enabled,
                    )
                    for m in maps
                ]
            )
    async_add_entities(sensors, update_before_add=True)


class NilanCTS602Sensor(SensorEntity, NilanEntity):
    """Representation of a Sensor."""

    def __init__(
        self,
        device,
        attribute,
        name,
        default_unit,
        device_class,
        state_class,
        entity_category,
        icon,
        enabled,
    ) -> None:
        """Init Sensor."""
        super().__init__(device)
        self._attribute = attribute
        self._device = device
        self._attr_native_unit_of_measurement = default_unit
        self._attr_device_class = device_class
        self._attr_state_class = state_class
        self._attr_entity_category = entity_category
        self._attr_icon = icon
        self._name = name
        self._attr_entity_registry_enabled_default = enabled
        self._attr_has_entity_name = True
        self._attr_translation_key = self._name
        self._attr_unique_id = self._name

    async def async_update(self) -> None:
        """Fetch new state data for the sensor."""
        self._attr_native_value = await getattr(self._device, self._attribute)()
