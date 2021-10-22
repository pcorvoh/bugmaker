# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021-07-18 15:32
# @Author   : 王俊
# @File     : single_node.py
# @Software : PyCharm

class Node():
    """节点"""

    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    '''
        is_empty():链表是否为空
        length():链表的长度
        travel()遍历链表
        add(item)链表头部添加元素
        append(item)链表尾部添加元素
        insert(pos,item)指定位置添加元素
        remove(item)删除元素
        serrch(item)查找元素
    '''

    def __int__(self, node: Node = None):
        self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """判断游标的长度"""
        # cur游标，用来遍历链表节点
        cur = self.__head
        # count计数
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.item, end=',')
            cur = cur.next

    def add(self, item):
        """头部添加元素(头插法)"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """尾部添加元素(尾插法)"""
        node = Node(item)
        if self.is_empty() is True:
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            pre = self.__head
            __count = 0
            while __count < (pos - 1):
                __count += 1
                pre = pre.next
            # 当退出循环后，pre指向pos-1的位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.item == item:
                # 先判断此节点是否是头节点
                # 头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找元素是否存在链表之中"""
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    pass
