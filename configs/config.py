# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021/5/16 18:10
# @Author   : 王俊
# @File     : config.py
# @Software : PyCharm

class BaseConfig(object):
    DEBUG = False
    LOG_LEVEL = "INFO"
    FORMART_LEVEL = "INFO"
    LOG_FORMAT = "%%(asctime)s - [%%(levelname)s] - %%(module)s - %%(name)s - %%(lineno)d - [日志信息]：%%(message)s"
    LOG_FORMAT_SMALL = "%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s"


class ProductionEnvironmentConfig(BaseConfig):
    pass


class TestEnvironmentConfig(BaseConfig):
    DEBUG = True
    LOG_LEVEL = "DEBUG"
    FORMART_LEVEL = "DEBUG"


class MyEnvironmentConfig(BaseConfig):
    DEBUG = True
    LOG_LEVEL = "DEBUG"
    FORMART_LEVEL = "DEBUG"
    DATABASE_NAME = "db_school"
    TBALE_NAME = "db_class"


environment_config = {
    "test_environment_config": TestEnvironmentConfig(),
    "my_environment_config": MyEnvironmentConfig(),
    "product_environment_config": ProductionEnvironmentConfig()
}
