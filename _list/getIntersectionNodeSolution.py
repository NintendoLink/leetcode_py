# python 3.6.4
# encoding: utf-8

"""
面试题 02.07. 链表相交

给定两个（单向）链表，判定它们是否相交并返回交点。请注意相交的定义基于节点的引用，而不是基于节点的值。换句话说，如果一个链表的第k个节点与另一个链表的第j个节点是同一节点（引用完全相同），则这两个链表相交。


示例 1：

输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

示例 2：

输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

示例 3：

输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。
"""
from _basestructure.list import ListNode
class Solution:

    """
    思路
    1、求长度即可
    """
    def getIntersectionNode(self, headA:ListNode, headB:ListNode):

        if headA is None or headB is None:
            return None

        lengthA = 0
        lengthB = 0
        pA = headA
        pB = headB
        while pA:
            lengthA += 1
            pA = pA.next
        while pB:
            lengthB += 1
            pB = pB.next

        if lengthA < lengthB:
            headA, headB = headB, headA
            lengthA,lengthB = lengthB,lengthA

        count = lengthA - lengthB
        while(count>0):
            headA = headA.next
            count -= 1

        while(headB and headA):
            if headB == headA:
                return headA
            headA, headB = headA.next, headB.next

        return None

if __name__ == '__main__':

    listA = ListNode(1)
    listA.next = ListNode(2)
    listA.next.next = ListNode(3)
    listA.next.next.next = ListNode(4)
    listA.next.next.next.next = ListNode(5)

    listB = ListNode(1)
    listB.next = listA.next
    # listB = ListNode(1)
    # listB = ListNode(1)
    # listB = ListNode(1)
    solution = Solution()
    print(solution.getIntersectionNode(listA,listB).val)