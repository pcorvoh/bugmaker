# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021/5/16 18:27
# @Author   : 王俊
# @File     : run_result.py
# @Software : PyCharm
class RunStatus:
    RUN = 1
    NO_RUN = 0
    WAIT = -1


class CaseResult:
    FAIL = 0
    PASS = 1
    SKIP = 2
    BLOCK = 3
    RELATE_NO_RUN = 4

    RELATE_FAIL = 10
    RELATE_PASS = 11
    RELATE_SKIP = 12
