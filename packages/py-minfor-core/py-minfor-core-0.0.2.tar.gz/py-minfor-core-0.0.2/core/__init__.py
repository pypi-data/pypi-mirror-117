import os

from core.setting import get_setting

DEFAULT = """
debug: true
server.mysql.host: mysql-server
server.mysql.port: 3306
server.mysql.user: root
server.mysql.charset: utf8
server.redis.host: redis-server
server.redis.port: 6379
server.redis.db: 0
server.mqtt.host: mqtt-server
server.mqtt.port: 1883
server.mqtt.keepalive: 60
server.celery.broker: amqp://guest:guest@rabbit-server:5672/vhost
server.celery.backend: redis://redis-server:6379/1
"""


def get_default_setting(default=DEFAULT):
    is_apollo = not os.environ.get('IS_APOLLO') == 'false'
    setting = get_setting(default, apollo=is_apollo)


def route_task(name: str, args, kwargs, options, task=None, **kw):
    names = name.split('.')
    if len(names) == 3 and names[0] == 'equipment':
        return {'queue': names[1]}


celery_update = dict(
    result_extended=True,
    result_expires=3600,
    timezone='Asia/Shanghai',
    task_routes=(route_task,),
)
