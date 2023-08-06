import redis


def get_redis_server(setting):
    pool = redis.ConnectionPool(
        host=setting.get('host'),
        port=int(setting.get('port', 6379)),
        db=int(setting.get('db', 0)),
        password=setting.get('password'),
        decode_responses=True
    )
    return redis.Redis(connection_pool=pool)
