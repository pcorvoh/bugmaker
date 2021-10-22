# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021-06-26 11:50
# @Author   : 王俊
# @File     : read_file.py
# @Software : PyCharm
from jsonpath import jsonpath


class ReadFile(object):

    @classmethod
    def extractor(cls, epr):
        """
            根据表达式提取字典中的value，表达式, . 提取字典所有内容， $.case 提取一级字典case， $.case.data 提取case字典下的data
            :param obj :json/dict类型数据
            :param expr: 表达式, . 提取字典所有内容， $.case 提取一级字典case， $.case.data 提取case字典下的data
            $.0.1 提取字典中的第一个列表中的第二个的值
            """