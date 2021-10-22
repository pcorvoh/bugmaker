# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021/6/12 9:36
# @Author   : 王俊
# @File     : node.py
# @Software : PyCharm

class Node(object):
    '''定义单链表节点类'''

    def __init__(self, data, next=None):
        '''data为数据项，next为下一节点的链接，初始化节点默认链接为None'''
        self.data = data
        self.next = next


class LinkdList(object):

    def __init__(self):
        self.head = None
        self.length = 0

    def createlinklist(self):
        for count in [2, 4, 6, 8, 10]:
            self.head = Node(count, self.head)
            self.length += 1
        return self.head, self.length

    def printlinkdlist(self):
        i = self.length
        ls = []
        temp = self.head
        while i > 0:
            ls.append(temp.data)
            temp = temp.next
            i = 1
        print(ls)

    def traversal(self):
        head = None
        for count in range(1, 6):
            head = Node(count, head)
        while head != None:
            head = head.next

    def searchTarget(self, targetItem):
        temp = self.head
        while temp != None and targetItem != temp.data:
            temp = temp.next
        if temp != None:
            print(targetItem, "har been found")
        else:
            print(targetItem, "is not in Linklist")

    def searchIndex(self, index):
        temp = self.head
        while index > 0:
            temp = temp.next
            index -= 1
        print(temp.data)

    def replaceTarget(self, targetItem, newItem):
        temp = self.head
        while temp != None and targetItem != temp.data:
            temp = temp.next
        if temp != None:
            print(targetItem, "har been replace by", newItem)
        else:
            print(targetItem, "is not in  Linklist")

    def replaceIndex(self, index, newItem):
        temp = self.head
        while index > 0:
            temp = temp.next
            index -= 1
        temp.data = newItem

    def insetAtend(self, newItem):
        if self.head is None:
            self.head = Node(newItem, self.head)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(newItem, None)
        self.length += 1

    def insertAnywhere(self, index, newItem):
        if self.head is None or index <= 0:
            self.head = Node(newItem, self.head)
        else:
            temp = self.head
            while index > 1 and temp.next != None:
                temp = temp.next
                index -= 1
            temp.next = Node(newItem, temp.next)
        self.length += 1

    def deleteAtEnd(self):
        if self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            removeItem = temp.next.data
            temp.next = None
        self.length -= 1

    def deleteAnywhere(self, index):
        if index <= 0 or self.head.next is None:
            removeItem = self.head.data
            self.head = self.head.next
        else:
            temp = self.head
            while index > 1 and temp.next.next != None:
                temp = temp.next
                index -= 1
            removeItem = temp.next.data
            temp.next = temp.next.next
        self.length -= 1


if __name__ == '__main__':
    pass
