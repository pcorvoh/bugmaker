# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021-10-22 16:35
# @Author   : UserName_Jack
# @File     : param_pool.py
# @Software : PyCharm
import os


class ParamsPoolMetaClass(type):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __getattr__(self, item):
        try:
            result = eval(os.environ.get(item.upper()))
        except (SyntaxError, TypeError, NameError, ValueError, KeyError) as SE:
            result = os.environ.get(item.upper())
        return result

    def __getattribute__(self, item: str):
        try:
            result = super().__getattribute__(item)
        except (AttributeError, RecursionError) as AE:
            try:
                result = eval(os.environ.get(item.upper()))
            except (SyntaxError, TypeError, NameError, ValueError, KeyError) as SE:
                result = os.environ.get(item.upper())

        return result

    def __setattr__(self, key: str, value):
        super().__setattr__(key, value)
        os.environ[key.upper()] = str(value)


class ParameterPoolNew(metaclass=ParamsPoolMetaClass):
    """
        参数池
    """

    def __getattr__(self, item):
        try:
            result = eval(os.environ.get(item.upper()))
        except (SyntaxError, TypeError, NameError, ValueError, KeyError) as SE:
            result = os.environ.get(item.upper())
        return result

    def __getattribute__(self, item: str):
        try:
            result = super().__getattribute__(item)
        except (AttributeError, RecursionError) as AE:
            try:
                result = eval(os.environ.get(item.upper()))
            except (SyntaxError, TypeError, NameError, ValueError, KeyError) as SE:
                result = os.environ.get(item.upper())
        return result

    def __setattr__(self, key: str, value):
        super().__setattr__(key, value)
        os.environ[key.upper()] = str(value)
