# python 3.6.4
# encoding: utf-8

"""
面试题 02.02. 返回倒数第 k 个节点
实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。

注意：本题相对原题稍作改动

示例：

输入： 1->2->3->4->5 和 k = 2
输出： 4
说明：

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from _basestructure.list import ListNode

class Solution:

    """
    思路
    1、快慢指针
    2、利用栈或者数组，将这个链表中的数据index化
    """
    def kthToLast(self,head,k):

        if head is None:
            return None

        fast = head
        slow = head

        while(k > 0):
            fast = fast.next
            k -= 1

        while(fast):
            fast = fast.next
            slow = slow.next
        return slow.val

        # if head is None:
        #     return None
        # container = []
        # while(head):
        #     container.append(head.val)
        #     head = head.next
        #
        # return container[len(container) - k]

if __name__ == '__main__':
    listA = ListNode(1)
    listA.next = ListNode(2)
    listA.next.next = ListNode(3)
    listA.next.next.next = ListNode(4)
    listA.next.next.next.next = ListNode(5)

    solution = Solution()
    print(solution.kthToLast(listA,2))