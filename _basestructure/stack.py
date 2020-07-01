# python 3.6.4
# encoding: utf-8

class ArrayStack:
    """
    利用数组实现栈
    """
    def __init__(self):
        # 栈的最大容量，容量可以设计成动态增加的形式
        self._max_capacity = 100

        # 容器，这里用list，并初始化，在下面的pop和push方法中，仅仅index来控制栈顶
        self._container = [0 for i in range(self._max_capacity)]
        # 栈顶指针
        self._pointer = -1

    # 入栈
    def push(self, obj):

        if self._pointer == self._max_capacity - 1:
            raise Exception("Can not be push in stack,Stack have reached MAX capacity")
        self._pointer += 1
        self._container[self._pointer] = obj

    # 出栈
    def pop(self):
        if self.is_empty():
            raise Exception("Can not be pop from EMPTY stack")

        obj = self._container[self._pointer]
        self._pointer -= 1
        return obj

    # 判空
    def is_empty(self):
        return self._pointer == -1

class ListStack:
    """
    使用链表实现栈
    """
    class _ListNode:
        def __init__(self,val):
            self.val = val
            self.next = None
    # 初始化
    def __init__(self):
        self._capacity = 0
        self._head = self._ListNode(None)
        self._pointer = self._head

    # 入栈,时间复杂度为o(1)
    def push(self,obj):
        node = self._ListNode(obj)
        self._pointer.next = node
        self._pointer = self._pointer.next
        self._capacity += 1

    # 出栈,可以看到，如果使用单链表的话，pop操作需要o(N)的时间复杂度，可以考虑使用双链表
    def pop(self):
        if(self.is_empty()):
           return None
        obj = self._pointer.val
        other = self._head
        while(other.next is not self._pointer):
            other = other.next

        self._pointer = other
        self._capacity -= 1
        return obj
    # 判空
    def is_empty(self):
        return self._pointer is self._head

if __name__ == '__main__':
    stack = ListStack()
    stack.push(1)
    stack.push(2)
    stack.push(2)
    stack.push(2)
    stack.push(2)
    stack.push(2)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
