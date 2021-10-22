# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021/6/12 19:07
# @Author   : 王俊
# @File     : billnode.py
# @Software : PyCharm

class Node(object):
    """结点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self, Node=None):
        self.__head = Node

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head
        cnt = 0
        while cur != None:
            cnt += 1
            cur = cur.next
        return cnt

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next

    def add(self, item):
        """插入头结点"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """插入尾节点"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head

            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pose, item):
        """在指定位置插入结点"""
        if pose <= 0:
            self.add(item)
        elif pose >= self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            cnt = 1
            cur = self.__head
            pre = None
            while cnt != pose:
                pre = cur
                cur = cur.next
                cnt += 1
            cur = node
            cur.next = pre.next
            pre.next = cur

    def remove(self, item):
        if self.is_empty():
            print("链表为空，删除操作错误！")
        else:
            cur = self.__head
            pre = None
            while cur.elem != item:
                pre = cur
                cur = cur.next
            pre.next = cur.next0
            print("删除成功！")
            del cur

    def search(self, item):
        cur = self.__head
        while cur.elem != item:
            cur = cur.next
        print("查找成功")
        pass


if __name__ == "__main__":
    l = SingleLinkList()
    print(l.is_empty())
    print(l.length())
    l.append(1)
    print(l.is_empty())
    print(l.length())
    l.add(0)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)

    l.append(6)
    l.insert(255, 100)
    l.travel()
