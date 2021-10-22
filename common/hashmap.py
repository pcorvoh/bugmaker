# !/user/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2021/6/8 11:27
# @Author   : 王俊
# @File     : hashmap.py
# @Software : PyCharm
"""
    Entry表示一个Key-value键值对节点，在Python中的dict里面叫做items。
"""


class Entry():
    def __init__(self, hash=0, key=0, value=0, next=None):
        self.hash = hash
        self.key = key
        self.value = value
        self.next = next


class HashMap():
    """
        初始化默认HashMap的容量是16，加载因子是0.75，也就是阈值是16 * 0.75 = 12，就会扩容
    """

    def __init__(self, capacity=16, load_factor=0.75):
        self.__capacity = capacity  # HashMap的容量
        self.__load_factor = load_factor  # 加载因子,
        self.__table = [None for i in range(capacity)]  # 创建一个空数组
        self.__size = 0  # HashMap中节点总数量
        self.__threshold = capacity * load_factor  # HashMap的阈值,超过这个阈值需要扩容

    """
        重写“toString()”方法，这样可以直接输出HashMap
    """

    def __str__(self):
        result = "{"
        count = 0
        for i in range(len(self.__table)):
            if (self.__table[i] != None):
                result += str(self.__table[i].key)
                result += ":"
                result += str(self.__table[i].value)
                if (count != self.__size - 1):
                    count += 1
                    result += ", "

        result += "}"
        return result

    """
        根据hash后的值 和 capacity, 得到下标
    Parameters:
		hash: 将key进行hash得到的Hash值
        capacity: 当前数组的长度
	Returns:
		index：数组下标，表示该元素应该放到哪个数组中去

    """

    def __index_for(self, hash, capacity):
        return hash & (self.__capacity - 1)

    """
        扩容后,将旧的list中的链表节点转移到新的list中去
    Parameters:
        new_table: 新创建的Hash表
    Retures: None
    """

    def __transfer(self, new_talbe):
        new_capacity = len(new_talbe)
        for e in self.__table:
            while (None != e):
                next = e.next
                i = self.__index_for(e.hash, new_capacity)
                e.next = new_talbe[i]
                new_talbe[i] = e
                e = next

    """
        扩容， 创建一个新的hash表，容量是new_capacity
        Parameters:
            new_capacity: 新Hash表的容量
    """

    def __resize(self, new_capacity):
        old_table = self.__table
        old_capacity = len(old_table)
        new_talbe = [Entry() for x in range(new_capacity)]
        self.__transfer(new_talbe)
        self.__table = new_talbe
        self.__threshold = self.__load_factor * self.__capacity

    """
        创建一个节点, 并且将节点使用头插法添加到链表中去
    """

    def __create_entry(self, hash, key, value, bucketIndex):
        e = self.__table[bucketIndex]
        self.__table[bucketIndex] = Entry(hash, key, value, e)
        self.__size += 1

    """
        通过计算key和hash值，将键值对放入到Hash表中去
    """

    def __add_entry(self, hash, key, value, bucket_index):
        # 如果元素过多,就需要扩容
        if ((self.__size >= self.__threshold) and (None != self.__table[bucket_index])):
            self.__resize(2 * len(self.__table))  # 将容量扩容成两倍
            hash = hash(key)
            bucket_index = self.__index_for(hash, len(self.__table))

        self.__create_entry(hash, key, value, bucket_index)

    """
        将key-value pair放入HashMap中
    """

    def put(self, key, value):
        h = hash(key)
        i = self.__index_for(h, self.__capacity)
        e = self.__table[i]
        while (e != None):
            k = e.key

            # 如果key在HashMap中已经存在了
            # 那么就把新的value覆盖旧的value,并且把旧的value返回出来
            if (e.hash == h and (k == key)):
                old_value = e.value
                e.value = value
                return old_value

            e = e.next

        self.__add_entry(h, key, value, i)
        return None

    """
        删除某个节点(Entry)
    """

    def __remove_entry_for_key(self, key):
        if (self.__size == 0): return None
        h = hash(key)
        i = self.__index_for(h, len(self.__table))
        prev = self.__table[i]
        e = prev

        while (e != None):
            next = e.next
            k = e.key
            if ((e.hash == h) or k == key):
                self.__size -= 1
                if (prev == e):
                    self.__table[i] = next
                else:
                    prev.next = next
                return e
            prev = e
            e = next
        return e

    def remove(self, key):
        e = self.__remove_entry_for_key(key)
        if (e == None):
            return None
        else:
            return e.value

    """
        get方法，通过key，得到value
    """

    def get(self, key):
        entry = self.__get_entry(key)
        if (entry == None):
            return None
        else:
            return entry.value

    """
        通过key，找到那个节点
    """

    def __get_entry(self, key):
        if (self.__size == 0): return None
        h = hash(key)
        e = self.__table[self.__index_for(h, len(self.__table))]
        while (e != None):
            k = e.key
            if ((e.hash == h) and e.key == k):
                return e
            e = e.next
        return None

if __name__ == '__main__':
    person = HashMap()
    person.put('name', 'Jackson')
    person.put('sex', 'male')
    person.put('age', '19')
    print(person)  # 输出完整信息
    person.remove('age')
    print(person)
