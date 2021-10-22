# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021/5/21 15:51
# @Author   : 王俊
# @File     : send_requests.py
# @Software : PyCharm
import requests
from requests import request, Session


class SendRequests(object):
    session = Session()

    def send(self, method: str, url, header, data=None, json=None, params=None):
        method = method.upper()
        if method == "GET":
            result = request(url=url, method=method, headers=header, data=data, json=json, params=params)
        elif method == "POST":
            result = request(url=url, method=method, headers=header, data=data, json=json, params=params)
        else:
            raise ValueError("没有该请求方法！")
        return result

    def send_session(self, method: str, url, header, data=None, json=None, params=None):
        method = method.upper()
        if method == "GET":
            result = self.session.request(url=url, method=method, headers=header, data=data, json=json, params=params)
        elif method == "POST":
            result = self.session.request(url=url, method=method, headers=header, data=data, json=json, params=params)
        else:
            raise ValueError("没有该请求方法！")
        return result


class Requests_Time(object):
    get_session = requests.session()

    def post_request(self, url, data, header):
        """
        Post请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:
            if data is None:
                response = self.get_session.post(url=url, headers=header)
            else:
                response = self.get_session.post(url=url, params=data, headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds / 1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts
