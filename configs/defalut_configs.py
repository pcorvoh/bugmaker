# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021/5/16 23:19
# @Author   : 王俊
# @File     : defalut_configs.py
# @Software : PyCharm
from werkzeug.datastructures import ImmutableDict

from configs.config import TestEnvironmentConfig, MyEnvironmentConfig, environment_config

STRING_TYPES = (str, list, tuple, dict, int, complex)


class DefaultConfig(dict):
    defaultconfig = ImmutableDict({})

    def __init__(self):
        dict.__init__(self, dict(self.defaultconfig) or {})

    def form_obj(self, obj):
        """
            传入一个对象，自动获取对象的实例属性
        :param obj:
        :return:
        """
        if isinstance(obj, STRING_TYPES):
            raise TypeError("请传入类可调用对象")
        elif hasattr(obj, "__class__"):
            for key in dir(obj):
                if key.isupper():
                    self[key] = getattr(obj, key)


config = DefaultConfig()
if __name__ == '__main__':
    # print(environment_config.get("test_environment_config"))
    # test = TestEnvironmentConfig()
    # my = MyEnvironmentConfig()
    # config.form_obj(test)
    config.form_obj(environment_config.get("test_environment_config"))
    print(config["LOG_FORMAT"])
