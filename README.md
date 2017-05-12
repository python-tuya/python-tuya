# Python Tuya

A library to read the state of Tuya based IoT devices e.g. [Goldair Heaters](http://www.goldair.co.nz/product-catalogue/heating/wifi-heaters/electronic-wi-fi-control-eco-panel-heater-geph205)

I have created this for use with [Home Assistant](https://home-assistant.io) components that I have yet to build. 

The heaters (possibly all Tuya based devices) run a TCP server on port 6668 (for control and getting the full state) which uses the same encrypted packets but my connections are dropped as soon as the socket is open. If anyone else has cracked this please let me know.

## Example usage

```python
>>> from pytuya.devices.heater import TuyaHeater
>>> heater1 = TuyaHeater('DEVICE_UID','DEVICE_PASSWORD','DEVICE_LOCAL_KEY','CLOUD_REGION')

>>> print(heater1.room_temperature())
20
>>> print(heater1.set_state())
True
```

