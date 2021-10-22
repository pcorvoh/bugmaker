# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021/5/16 19:56
# @Author   : 王俊
# @File     : resopnse_assert.py
# @Software : PyCharm

def compare_json_data(A, B, xpath='.'):
    if isinstance(A, list) and isinstance(B, list):
        for i in range(len(A)):
            try:
                compare_json_data(A[i], B[i], xpath + '[%s]' % str(i))
            except:
                print('▇▇▇▇▇ A中的%s[%s]未在B中找到' % (xpath, i))
    if isinstance(A, dict) and isinstance(B, dict):
        for i in A:
            try:
                B[i]
            except:
                print('▇▇▇▇▇ A中的%s/%s 未在B中找到' % (xpath, i))
                continue
            if not (isinstance(A.get(i), (list, dict)) or isinstance(B.get(i), (list, dict))):
                if type(A.get(i)) != type(B.get(i)):
                    print('▇▇▇▇▇ 类型不同参数在[A]中的绝对路径:  %s/%s  ►►► A is %s, B is %s ' % (
                        xpath, i, type(A.get(i)), type(B.get(i))))
                elif A.get(i) != B.get(i):
                    print('▇▇▇▇▇ 仅内容不同参数在[A]中的绝对路径:  %s/%s  ►►► A is %s, B is %s ' % (xpath, i, A.get(i), B.get(i)))
                continue
            compare_json_data(A.get(i), B.get(i), xpath + '/' + str(i))
        return
    if type(A) != type(B):
        print('▇▇▇▇▇ 类型不同参数在[A]中的绝对路径:  %s  ►►► A is %s, B is %s ' % (xpath, type(A), type(B)))
    elif A != B and type(A) is not list:
        print('▇▇▇▇▇ 仅内容不同参数在[A]中的绝对路径:  %s  ►►► A is %s, B is %s ' % (xpath, A, B))


if __name__ == '__main__':
    # print(compare_json_data())
    pass
