# python 3.6.4
# encoding: utf-8

"""
21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from list import ListNode
class Solution:
    """
    思路：普通遍历即可
    """
    def mergeTwoLists(self, l1, l2):

        head = ListNode(None)
        res = head
        while(l1 and l2):

            if l1.val <= l2.val:
                res.next = ListNode(None)
                res = res.next
                res.val = l1.val
                l1 = l1.next

            else:
                res.next = ListNode(None)
                res = res.next
                res.val = l2.val
                l2 = l2.next

        # 这边可以写成if的形式
        while(l1):
            res.next = ListNode(None)
            res = res.next
            res.val = l1.val
            l1 = l1.next
        while(l2):
            res.next = ListNode(None)
            res = res.next
            res.val = l2.val
            l2 = l2.next
        return head.next

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(5)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(2)
    node5 = ListNode(4)
    node4.next = node5

    solution = Solution()

    ListNode.printall(solution.mergeTwoLists(node1,node4))

    pass