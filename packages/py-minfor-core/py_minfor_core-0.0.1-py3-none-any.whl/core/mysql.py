import pymysql

from dbutils.pooled_db import PooledDB


def get_mysql_pool(setting):
    mysql_pool = PooledDB(
        creator=pymysql,
        cursorclass=pymysql.cursors.DictCursor,
        host=setting.get('host', 'localhost'),
        port=int(setting.get('port', 3306)),
        user=setting.get('user', 'root'),
        password=setting.get('password', ''),
        charset=setting.get('charset', 'utf8'),
    )
    return mysql_pool
