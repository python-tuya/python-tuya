from pytuya.devices.base import TuyaDevice

class TuyaHeater(TuyaDevice):
    """
    Represents a Tuya Heater.
    """

    def __init__(self, id, password, local_key, region):
        super(TuyaHeater, self).__init__(id, password, local_key, region)

    def state(self):
        return self._last_reading.get('1', False)

    def is_on(self):
        return self.state()

    def setting_temperature(self):
        return self._last_reading.get('3', None)
    
    def room_temperature(self):
        return self._last_reading.get('4', None)

    def key_lock(self):
        return self._last_reading.get('2', False)

    def timer(self):
        return self._last_reading.get('5', 0)

    def object_type(self):
        return "Heater"