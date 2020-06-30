# python 3.6.4
# encoding: utf-8
"""
不使用任何内建的哈希表库设计一个哈希集合

具体地说，你的设计应该包含以下的功能

add(value)：向哈希集合中插入一个值。
contains(value) ：返回哈希集合中是否存在这个值。
remove(value)：将给定值从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

示例:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);        
hashSet.add(2);        
hashSet.contains(1);    // 返回 true
hashSet.contains(3);    // 返回 false (未找到)
hashSet.add(2);          
hashSet.contains(2);    // 返回 true
hashSet.remove(2);          
hashSet.contains(2);    // 返回  false (已经被删除)

注意：

所有的值都在 [0, 1000000]的范围内。
操作的总数目在[1, 10000]范围内。
不要使用内建的哈希集合库。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-hashset
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import random

class MyHashSet():
    """
    简单思路：
        1、使用固定大小的数组+链表实现
    复杂思路：
        1、使用动态大小的数组+链表实现
        2、数组的大小和查询的时间保持动态平衡
    """
    class Node:
        def __init__(self,val = None):
            self.val = val
            self.next = None

    def __init__(self):

        # 容器的初始大小
        self._capacity = 64

        # 容器的数据结构 数组+链表
        self._container = [self.Node() for _ in range(self._capacity)]

    def add(self,key):
        index = key % self._capacity

        # 1、链表中不存在，且链表为空
        if self._container[index].next is None:
            self._container[index].next = self.Node(key)
            return
        node = self._container[index]
        while(node.next is not None):
            #2、链表中已经存在
            if node.next.val == key:
                return
            node = node.next

        # 3、链表中不存在，链表不为空，已经遍历到链表尾
        node.next = self.Node(key)

    def contains(self,key):

        # 1、数组为空，不存在
        index = key % self._capacity
        node = self._container[index]
        while(node.next is not None):
            # 2、数组不为空，遍历后存在
            if node.next.val == key:
                return True
            node = node.next
        # 3、数组不为空，遍历后不存在
        return False

    def remove(self,key):
        # 1、数组为空，不存在，不用删除操作
        index = key % self._capacity
        if self._container[index].next is None:
            return False

        node = self._container[index]
        while(node.next is not None):

            # 2、数组不为空，遍历后存在，需要删除，链表之间的删除
            if node.next.val == key:

                # 2.1、需要删除的元素不是链表的最后一个
                if node.next.next is not None:
                    node.next = node.next.next
                    return True
                # 2.2需要删除的元素是链表的最后一个
                else:
                    node.next = None
                    return True
            node = node.next
        # 3、数组不为空，遍历后不存在，不用删除操作
        return False

    def listnode2list(self,node):
        ls = []
        while(node.next is not None):
            ls.append(node.next.val)
            node = node.next
        return ls

    def printAll(self):
        for i in range(self._capacity):
            node = self._container[i]
            while(node.next is not None):
                print(node.next.val)
                node = node.next

if __name__ == '__main__':
    hashset = MyHashSet()

    for i in range(1000):
        hashset.add(i)
    # hashset.printAll()
    #
    #
    for i in range(1000):
        key = random.randint(0,1000)
        print(hashset.remove(key))
    # print(hashset.contains(72))
    # print(hashset.remove(91))
    # print(hashset.add(48))
    # print(hashset.add(41))
    # print(hashset.contains(96))