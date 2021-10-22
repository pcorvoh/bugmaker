# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021/5/16 17:57
# @Author   : 王俊
# @File     : read_config.py
# @Software : PyCharm
import os
import yaml
from common import CONF_DIR


class ReadeConfig(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, f):
        """ 此类用于读取配置文件信息，配置文件采用yaml形式
        :param f: config配置文件的配置文件名称
        """
        self.filename = os.path.join(CONF_DIR, f)
        self._data = None

    def get(self, key=None, index=0, hot=False) -> dict:
        """ 用于获取配置文件某个值
        :param key: 需要获取的配置文件项
        :param index: 索引，配置项以‘---’分隔，默认为0
        :param hot:热加载配置，默认为False不启动,True表示每次都从文件中读取数据
        :return: 返回配置项信息
        """
        if self._data is None or hot:
            with open(self.filename, "rb") as f:
                self._data = list(yaml.safe_load_all(f))
            if key is None:
                return self._data[index]
            else:
                return self._data[index][key]


conf = ReadeConfig("dbconfig.yaml").get()
base_conf = ReadeConfig("baseconfig.yaml")


def select_db(db_type):
    db_map = {
        "weijian": conf.get("WeiJianDBConfig"),
        "mydb": conf.get("MyDBConfig"),
        "dbpoolmaster": conf.get("MyDBConfig"),
        "dbpoollocal": conf.get("DBPoolLocalHostConfig"),
    }
    db_conf = db_map.get(db_type)
    return db_conf
