# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021/5/16 17:43
# @Author   : 王俊
# @File     : run.py
# @Software : PyCharm

import os
import shutil
from test.conftest import pytest
from common.excute_log import run_log
from tools.read_file import ReadFile
from tools.send_email import EmailServe

file_path = ReadFile.read_config('$.file_path')
email = ReadFile.read_config('$.email')


def run():
    if os.path.exists('report/'):
        shutil.rmtree(path='report/')
    run_log.info("""
                 _    _         _      _____         _
  __ _ _ __ (_)  / \\  _   _| |_ __|_   _|__  ___| |_
 / _` | '_ \\| | / _ \\| | | | __/ _ \\| |/ _ \\/ __| __|
| (_| | |_) | |/ ___ \\ |_| | || (_) | |  __/\\__ \\ |_
 \\__,_| .__/|_/_/   \\_\\__,_|\\__\\___/|_|\\___||___/\\__|
      |_|
      Starting      ...     ...     ...
    """)
    pytest.main(
        args=[
            'test/test_api.py',
            f'--alluredir={file_path["report"]}/data'])
    # 自动以服务形式打开报告
    # os.system(f'allure serve {report}/data')

    # 本地生成报告
    os.system(
        f'allure generate {file_path["report"]}/data -o {file_path["report"]}/html --clean')
    run_log.success('报告已生成')

    # # 发送邮件带附件报告
    # EmailServe.send_email(email, file_path['report'])
    #
    # # 删除本地附件
    # os.remove(email['enclosures'])


if __name__ == '__main__':
    run()