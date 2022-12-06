from .abstract_intent import AbstractIntent


class AbstractStatisticIntent(AbstractIntent):
    sensor_name = None
    sensor_key = None
    sensor_unit = None
    interval = None

    def generate_response(self) -> str:
        module_name, module_index = self.get_module_data()
        sensor_average = self._get_sensor_average(module_index)
        return f"Average {self.sensor_name} in module {module_name} for the past {self.interval} is {sensor_average} " \
               f"{self.sensor_unit}"

    def _get_sensor_average(self, module_index: int) -> int:
        value = self._get_measurements(module_index, self.sensor_key)
        if value:
            return value
        # TODO: error


class TemperatureStatisticIntent(AbstractStatisticIntent):
    sensor_name = "water temperature"
    sensor_key = "water_temperature"
    sensor_unit = "degrees Celsius"


class PHStatisticIntent(AbstractStatisticIntent):
    sensor_name = "water pH"
    sensor_key = "ph"
    sensor_unit = "pH"


class TDSStatisticIntent(AbstractStatisticIntent):
    sensor_name = "TDS value"
    sensor_key = "tds"
    sensor_unit = "parts per million"


class ECIntent(AbstractStatisticIntent):
    sensor_name = "electrical conductivity value"
    sensor_key = "ec"
    sensor_unit = "Ohm meters"

