# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021/5/16 19:47
# @Author   : 王俊
# @File     : excute_log.py
# @Software : PyCharm
import os
from typing import Union, Optional
from common import LOG_DIR
from loguru import logger


#  安装concurrent-log-handler

class DoLog(object):
    LOGNAME = "logfile.log"
    ROTATION = "00:00"
    COLORIZE = True
    BACKTRACE = True
    LOG_FORMAT = "{time:YYYY-MM-DD | HH:mm:ss} | {level} | {message}"
    # "{time:YYYY-MM-DD | HH:mm:ss} | {level} | {message}"
    LOG_DIAGNOSE = True
    LOG_ENCODING = "UTF-8"
    RETENTION = "10 days"
    ENQUEUE = False
    DIAGNOSE = True
    COMPRESSION = "zip"  # 压缩日志，暂时为使用到

    def do_log(
            self,
            rotation: Union[str] = ROTATION,
            colorize: Optional[bool] = COLORIZE,
            backtrace: Optional[bool] = BACKTRACE,
            format: Union[str] = LOG_FORMAT,
            diagnose: bool = DIAGNOSE,
            encoding: str = LOG_ENCODING,
            retention=RETENTION,
            enqueue=ENQUEUE
    ) -> logger:
        """输出日志文件"""
        logger.add(
            os.path.join(LOG_DIR, self.LOGNAME),
            rotation=rotation,
            colorize=colorize,
            backtrace=backtrace,
            format=format,
            diagnose=diagnose,
            encoding=encoding,
            retention=retention,
            enqueue=enqueue
        )
        return logger


do_log = DoLog().do_log()

if __name__ == '__main__':
    # log = ExcuteLog()
    pass
