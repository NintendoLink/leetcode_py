
"""
队列实现栈
225. 用队列实现栈
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:

你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
通过次数59,119提交次数91,047

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-stack-using-queues
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from queue import Queue

class MyStack:

    """
    valid operation：
     push to back
     peek/pop from front,
     size,
     is empty
     思路：
     1、用两个队列实现栈
     2、用单队列实现、不过需要反转队列
    """
    def __init__(self):

        """
        Initialize your data structure here.
        """
        self._container = Queue()
        self._temp_container = Queue()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self._container.put(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return None
        while(self._container.qsize() >1):
            self._temp_container.put(self._container.get())

        res = self._container.get()
        temp = self._container
        self._container =self._temp_container
        self._temp_container = temp
        return res

    def top(self) -> int:
        """
        Get the top element.
        """
        pop = self.pop()
        self._container.put(pop)
        return pop


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self._container.empty()
if __name__ == '__main__':

    stack = MyStack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack.top())
    print(stack.pop())
    print(stack.top())

