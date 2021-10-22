# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021-06-25 20:10
# @Author   : 王俊
# @File     : hook.py
# @Software : PyCharm

class MyStack():
    __slots__ = ("__stack")

    def __init__(self):
        self.__stack = []

    def is_empty(self):
        return self.__stack == []

    def peek(self):
        return self.__stack[len(self.__stack) - 1]

    def size(self):
        return len(self.__stack)

    def push(self, item):
        self.__stack.append(item)

    def pop(self, item):
        self.__stack.pop(item)
