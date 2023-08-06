# 使用文档

将此项目放置在根目录 core 下，参考示例脚本使用即可。

### 示例脚本
```
import os

from core.celery import get_celery_server
from core.logging import init_logging
from core.mqtt import get_mqtt_server
from core.mysql import get_mysql_pool
from core.redis import get_redis_server
from core.setting import get_setting

# 初始配置
DEFAULT = """
debug: true
server.mysql.host: 127.0.0.1
server.mysql.port: 3306
server.mysql.user: root
server.mysql.charset: utf8
server.redis.host: 127.0.0.1
server.redis.port: 6379
server.redis.db: 0
server.mqtt.host: 127.0.0.1
server.mqtt.port: 1883
server.mqtt.keepalive: 60
server.celery.broker: amqp://guest:guest@127.0.0.1:5672/vhost
server.celery.backend: redis://127.0.0.1:6379/1
"""

# 配置环境
os.environ.setdefault('ENV_PREFIX_APOLLO', 'APOLLO')
os.environ.setdefault('APOLLO_URI', 'http://192.168.68.251:8080')
os.environ.setdefault('APOLLO_APPID', 'equipment-services')

# 初始化日志
init_logging()

# 获取配置
setting = get_setting(DEFAULT)

# 打印配置
print(setting.get().__dict__)
print(setting.get('debug'))

# 服务初始化
redis_server = get_redis_server(setting.get('server.redis'))
mysql_pool = get_mysql_pool(setting.get('server.mysql'))
mysql_server = mysql_pool.connection()
celery_server = get_celery_server(setting.get('server.celery'))
mqtt_server = get_mqtt_server(setting.get('server.mqtt'))
```
