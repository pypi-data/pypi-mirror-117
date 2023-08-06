import celery


def get_celery_server(options):
    """获取 Celery 服务"""
    celery_server = celery.Celery(
        broker=options.get('broker'),
        backend=options.get('backend'),
    )
    celery_server.conf.update(
        result_extended=True,
        result_expires=3600,
        timezone='Asia/Shanghai',
    )
    return celery_server
