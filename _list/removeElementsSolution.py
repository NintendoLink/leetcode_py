# python 3.6.4
# encoding: utf-8

"""
203. 移除链表元素
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""
from _basestructure.list import ListNode


class Solution:
    """
    思路：使用哨兵节点，使得链表用不为空
    """

    def removeElements(self, head: ListNode, val: int) -> ListNode:

        # # 错误代码,无法找到前节点。对于ListNode的置空并不能用node = None.node是一个指针，指针置空，真是的node并不会置空，在链表中，
        # 置空意味着prev.next = None
        # pHead = head
        #
        # while(head):
        #     if head.val == val:
        #         if head.next:
        #             head.val = head.next.val
        #             head.next = head.next.next
        #
        #         else:
        #             head = None
        #         return pHead
        #     head = head.next
        #
        # return pHead
        pHead = ListNode(None)
        pHead.next = head
        res = pHead

        while(pHead.next):

            if pHead.next.val == val:
                pHead.next = pHead.next.next
                continue
            pHead = pHead.next
        return res.next
    # def removeElements(self, head: ListNode, val: int) -> ListNode:
    #     sentinel = ListNode(0)
    #     sentinel.next = head
    #
    #     prev, curr = sentinel, head
    #     while curr:
    #         if curr.val == val:
    #             prev.next = curr.next
    #         else:
    #             prev = curr
    #         curr = curr.next
    #
    #     return sentinel.next


if __name__ == '__main__':
    solution = Solution()
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)

    node.next.next.next = ListNode(3)
    node.next.next.next.next = ListNode(4)
    node.next.next.next.next.next = ListNode(5)
    node.next.next.next.next.next.next = ListNode(6)
    head = solution.removeElements(node,3)

    while(head):
        print(head.val)
        head = head.next
