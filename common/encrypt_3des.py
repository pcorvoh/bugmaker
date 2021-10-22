# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021-06-25 15:49
# @Author   : 王俊
# @File     : encrypt_3des.py
# @Software : PyCharm
from Cryptodome.Cipher import DES3
import codecs
import base64

class EncryptDate:
    def __init__(self, key):
        self.key = key  # 初始化密钥
        self.length = DES3.block_size  # 初始化数据块大小
        self.aes = DES3.new(self.key, DES3.MODE_CBC, b'01234567')  # 初始化AES,ECB模式的实例
        # 截断函数，去除填充的字符
        self.unpad = lambda date: date[0:-ord(date[-1])]

    def pad(self, text):
        """
        #填充函数，使被加密数据的字节码长度是block_size的整数倍
        """
        count = len(text.encode('utf-8'))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt(self, encrData):  # 加密函数
        res = self.aes.encrypt(self.pad(encrData).encode("utf8"))
        msg = str(base64.b64encode(res), encoding="utf8")
        msg =  res.hex()
        return msg

    def decrypt(self, decrData):  # 解密函数
        res = base64.decodebytes(decrData.encode("utf8"))
        # res = bytes.fromhex(decrData)
        msg = self.aes.decrypt(res).decode("utf8")
        return self.unpad(msg)


# eg = EncryptDate(r"*|rX<xO7<6B}7PA])?dN8fgX}wOr'HQh")  # 这里密钥的长度必须是16的倍数
# res = eg.encrypt("zhangs")
# print(res)
eg1 = EncryptDate(r"*|rX<xO7<6B}7PA])?dN8fgX")
"""
遇到的问题:
Java版本的desede/CBC/PKCS5Padding使用超过24位的key是不会报错的，代码会自动取前面24位
解决方法，把密钥只保留前24位数
"""
print(eg1.decrypt("Qy9NcvR6hM99rNZIMNU5gSVpmVdumdZ6h7QW6FBs/yh7kAlc26aQ/w=="))
