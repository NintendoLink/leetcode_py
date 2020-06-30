# python 3.6.4
# encoding: utf-8
"""

不使用任何内建的哈希表库设计一个哈希映射

具体地说，你的设计应该包含以下的功能

put(key, value)：向哈希映射中插入(键,值)的数值对。如果键对应的值已经存在，更新这个值。
get(key)：返回给定的键所对应的值，如果映射中不包含这个键，返回-1。
remove(key)：如果映射中存在这个键，删除这个数值对。

示例：

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);
hashMap.put(2, 2);
hashMap.get(1);            // 返回 1
hashMap.get(3);            // 返回 -1 (未找到)
hashMap.put(2, 1);         // 更新已有的值
hashMap.get(2);            // 返回 1
hashMap.remove(2);         // 删除键为2的数据
hashMap.get(2);            // 返回 -1 (未找到)

注意：

所有的值都在 [0, 1000000]的范围内。
操作的总数目在[1, 10000]范围内。
不要使用内建的哈希库。
"""
import random
class MyHashMap:

    """
    和hashset的思路一样，也是使用简单固定长度数组 + 链表
    """
    class MapEntry:
        def __init__(self,key,value):
            self.key = key
            self.value = value
    class Node:

        def __init__(self,entry = None):
            self.entry = entry
            self.next = None

    def __init__(self):
        self._capacity = 8
        self._contrainer = [self.Node() for _ in range(self._capacity)]

    def put(self,key,value):

        index = key % self._capacity

        # 1、链表为空,直接插入
        if self._contrainer[index].next is None:
            entry = self.MapEntry(key, value)
            self._contrainer[index].next = self.Node(entry)
            return True
        node = self._contrainer[index]
        # 2、key已经存在，需要将value替换掉
        while(node.next is not None):
            if node.next.entry.key == key:
                node.next.entry.value = value
                return False
            node = node.next

        # 3、遍历整个链表，仍然不存在，利用插入尾部
        entry = self.MapEntry(key, value)
        node.next = self.Node(entry)

    def get(self,key):

        index = key % self._capacity
        node = self._contrainer[index]

        # 1、遍历链表，找到了就返回key对应的value
        while(node.next is not None):
            if (node.next.entry.key == key):
                return node.next.entry.value
            node = node.next

        # 没有找到，返回-1
        return -1

    def remove(self,key):
        index = key % self._capacity
        node = self._contrainer[index]

        # 1、遍历链表
        while(node.next is not None):
            # 2、找到了对应的key
            if(node.next.entry.key == key):
                # 2.1、此时，node.next是最后一个节点,直接将其变为None即可
                if node.next.next is None:
                    node.next = None
                    return True
                # 2.2、不是最后一个节点，需要进行删除操作
                else:
                    node.next = node.next.next
                    return True
            node = node.next
        return False
    def printAll(self):

        for index in range(self._capacity):
            node = self._contrainer[index]
            while(node.next is not None):
                print("key:{},value:{}".format(node.entry.key,node.entry.value))
                node = node.next
if __name__ == '__main__':

    myhashmap = MyHashMap()
    for i in range(1000):
        myhashmap.put(i,i)

    for i in range(1000):
        rand = random.randint(0,1000)
        # print(myhashmap.get(rand))
        print(myhashmap.remove(rand))
