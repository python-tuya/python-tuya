import json
import paho.mqtt.client as mqtt
from pytuya.aes_cipher import AESCipher

class TuyaDevice(object):
    """
    This is a generic Tuya device, all other object inherit from this.
    """

    def __init__(self, id, password, local_key, region):
        """
        :type id string:
        :type password string:
        :type local_key string:
        :type region string:
        :return:
        """
        self.json_state = {}
        self.obj_id = id
        self.mqtt_pass = password
        self.local_key = local_key
        if region not in ['us', 'eu', 'cn']:
            raise ValueError("Region must be one of us, eu or cn")
        self.mqtt_server = "mq.gw.tuya{}.com".format(region)
        self.cipher = AESCipher(self.local_key)

        def on_connect(client, userdata, flags, rc):
            topic = "smart/mb/in/{}".format(self.obj_id)
            client.subscribe(topic)

        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = self.__on_mqtt_message

        client.username_pw_set(id, password)
        client.connect(self.mqtt_server, 1883, 60)
        client.loop_start()

    def __on_mqtt_message(self, client, userdata, msg):
        payload = str(msg.payload)[21:-1]
        decoded = self.cipher.decrypt(payload)
        update = json.loads(decoded)['data']['dps']
        for key in update:
            self.json_state[key] = update[key]

    def state(self):
        return self.json_state

    def object_id(self):
        return self.obj_id

    def object_type(self):
        raise NotImplementedError("Must implement object_type")

    @property
    def _last_reading(self):
        return self.json_state or {}
