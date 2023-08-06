import paho.mqtt.client


def get_mqtt_server(options):
    """获取 MQTT 服务"""
    mqtt_server = paho.mqtt.client.Client(
        client_id=options.get('client_id'),
    )
    mqtt_server.username_pw_set(
        options.get('username'),
        options.get('password'),
    )
    mqtt_server.connect(
        options.get('host', '127.0.0.1'),
        port=int(options.get('port', 1883)),
        keepalive=int(options.get('keep_alive', 60)),
    )
    return mqtt_server
