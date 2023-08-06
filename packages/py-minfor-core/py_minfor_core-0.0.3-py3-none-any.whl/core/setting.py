import requests
import yaml
from ApolloConfig import ApolloConfig


def get_setting(default='', prefix='project', apollo=True):
    """加载配置"""
    defaults = yaml.load(default, Loader=yaml.FullLoader)
    setting = ApolloConfig(prefix)
    for key, value in defaults.items(): setting.registry.set(key, value)
    try:
        setting.init(apollo)
    except requests.exceptions.ConnectionError:
        pass
    return setting
