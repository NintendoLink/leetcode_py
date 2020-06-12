# python 3.6.4
# encoding: utf-8
from list import ListNode
"""
83. 删除排序链表中的重复元素
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    """
    思路
    1、双指针解法
    2、单指针
    """
    # def deleteDuplicates(self,head):
    #
    #     # # 双指针解法
    #     # pivot1 = head
    #     # pivot2 = head
    #     # while(pivot1):
    #     #     if (pivot2.next is not None) :
    #     #         if (pivot2.val == pivot2.next.val):
    #     #             temp = pivot2.val
    #     #             while(pivot2):
    #     #                 if pivot2.val!= temp:
    #     #                     break
    #     #                 else:
    #     #                     pivot2 = pivot2.next
    #     #             if(pivot2):
    #     #                 pivot1.next = pivot2
    #     #                 pivot1 = pivot2
    #     #                 continue
    #     #             else:
    #     #                 pivot1.next = pivot2
    #     #                 return head
    #     #     pivot1 = pivot1.next
    #     #     pivot2 = pivot2.next
    #     # return head
    def deleteDuplicates(self,head):

        if head == None or head.next == None:
            return head
        # 单指针解法
        p = head

        while(p.next):
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head
if __name__ == '__main__':

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(2)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    solution = Solution()
    # ListNode.printall(node1)
    ListNode.printall(solution.deleteDuplicates(node1))