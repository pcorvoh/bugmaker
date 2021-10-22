# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021/5/16 17:41
# @Author   : 王俊
# @File     : __init__.py.py
# @Software : PyCharm
import os

# BASE_DIR = os.path.abspath(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

CONFIG_DIR = os.path.join(BASE_DIR, "configs")

REPORTS_DIR = os.path.join(BASE_DIR, "reports")

LOG_DIR = os.path.join(BASE_DIR, "log")

TESTCASE_DIR = os.path.join(BASE_DIR, "testcases")

CONF_DIR = os.path.join(BASE_DIR, "conf")

DEBUG_LOG_DIR = os.path.join(LOG_DIR, "DEBUG_LOG")

INFO_LOG_DIR = os.path.join(LOG_DIR, "INFO_LOG")

ERROR_LOG_DIR = os.path.join(LOG_DIR, "ERROR_LOG")

CRITICAL_LOG_DIR = os.path.join(LOG_DIR, "CRITICAL_LOG")

LOG_LEVE_FILE = {
    "DEBUG": DEBUG_LOG_DIR,
    "INFO": INFO_LOG_DIR,
    "ERROR": ERROR_LOG_DIR,
    "CRITICAL": CRITICAL_LOG_DIR,
}
for key, value in LOG_LEVE_FILE.items():
    if os.path.exists(value) is False:
        os.mkdir(value)
