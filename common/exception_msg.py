# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021/6/5 11:59
# @Author   : 王俊
# @File     : exception_msg.py
# @Software : PyCharm

class DataBaseException(Exception):
    def __init__(self, error="数据库连接异常!"):
        Exception.__init__(self, error)


class LogException(Exception):
    def __init__(self, error="日志写入异常!"):
        Exception.__init__(self, error)


class ConfException(Exception):
    def __init__(self, error="配置文件读取异常！"):
        Exception.__init__(self, error)


class ReadDataException(Exception):
    def __init__(self, error="测试用例读取异常！"):
        Exception.__init__(self, error)


class RequestException(Exception):
    def __init__(self, error="请求发送异常！"):
        Exception.__init__(self, error)


class UpdateException(Exception):
    def __init__(self, error="更新值错误！"):
        Exception.__init__(self, error)


class AssertException(Exception):
    def __init__(self, error="断言失败!"):
        Exception.__init__(self, error)


if __name__ == '__main__':
    def raiseex():
        raise DataBaseException()


    try:
        raiseex()
    except DataBaseException as D:
        print(D)
