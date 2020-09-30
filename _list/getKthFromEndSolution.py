
class ListNode:

    def __init__(self,x):
        self.val = x
        self.next = None

"""
剑指 Offer 22. 链表中倒数第k个节点

输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

 

示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.
"""
class Solution:
    """
    思路
    1、快慢指针
    2、普通算法
    """
    def getKthFromEnd(self,head:ListNode,k:int):
        """
        快慢指针
        """
        fast = head # 快指针
        slow = head # 慢指针

        for i in range(0,k):
            if not fast:
                return 0
            fast = fast.next

        while(fast):
            fast = fast.next
            slow = slow.next
        return slow

    def getKthFromEnd2(self, head:ListNode, k:int):

        head_cp = head

        ls_count = 0
        while(head_cp):
            ls_count += 1
            head_cp = head_cp.next

        iter_count = ls_count - k
        result = head
        for i in range(0,iter_count):
            result = result.next

        return result


if __name__ == '__main__':
    solution = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4


    print(solution.getKthFromEnd(node1,2).val)