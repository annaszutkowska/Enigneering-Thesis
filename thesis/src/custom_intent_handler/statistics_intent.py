from .abstract_intent import AbstractIntent


class AbstractStatisticIntent(AbstractIntent):
    sensor_name = None
    sensor_key = None
    sensor_unit = None

    def generate_response(self) -> str:
        module_name, module_index = self.get_module_data()
        sensor_average = self._get_sensor_average(module_index)
        return f"Average {self.sensor_name} in module {module_name} is {sensor_average:.2f} {self.sensor_unit}"

    def get_module_statistics(self, module_id: int,
                              start_date: str = None, end_date: str = None, count: str = None) -> list:
        statistics = self.connector.get_module_history(module_id, start_date, end_date, count)
        return [float(item[self.sensor_key]) for item in statistics]

    def _get_sensor_average(self, module_index: int) -> float:
        values = self.get_module_statistics(module_index)
        return sum(values)/len(values)


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


class ECStatisticIntent(AbstractStatisticIntent):
    sensor_name = "electrical conductivity value"
    sensor_key = "ec"
    sensor_unit = "Ohm meters"

