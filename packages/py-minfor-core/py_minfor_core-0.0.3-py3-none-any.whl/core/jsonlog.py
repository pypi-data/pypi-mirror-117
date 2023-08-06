import json
import os.path
import socket
import uuid
from inspect import getframeinfo, stack

import arrow


class JsonLog(object):
    def __init__(self, redis_server):
        self.redis_server = redis_server

    def write(self, options):
        caller = getframeinfo(stack()[1][0])
        filename = os.path.basename(caller.filename)
        lineno = caller.lineno

        data = dict()
        data['datetime'] = str(arrow.utcnow().to('Asia/Shanghai'))
        data['source_id'] = str(uuid.uuid4())
        data['source'] = options.get('source', 'unknown')
        data['host'] = socket.gethostname()
        data['level'] = options.get('level', 'debug')
        data['event'] = options.get('event', 'default')
        data['file_line'] = '%s:%s' % (filename, lineno)
        data['msg'] = options.get('msg', '')
        data['data'] = options.get('data', dict())
        self.redis_server.rpush('log:list', json.dumps(data))
