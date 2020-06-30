# python 3.6.4
# encoding: utf-8
"""
141. 环形链表
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from _basestructure.list import ListNode

class Solution:

    """
    思路1
    1、用一个哈希表存储已经访问过的节点，用来判断环
    2、利用快慢指针的方法来检测，本题只返回是否存在环形节点，可以升级到检测环形入口
    """

    # # 利用快慢指针的算法
    # def hasCycle(self,head):
    #
    #     if (head == None or head.next == None):
    #         return False
    #     slow = head.next
    #     fast = head.next.next
    #
    #     while(slow is not None and fast is not None):
    #         if (slow.val == fast.val):
    #             return True
    #         slow = slow.next
    #         if fast.next is not None:
    #             fast = fast.next.next
    #         else:
    #             return False
    #     return False

    # 哈希算法，利用python内置的list作为hash容器
    def hasCycle(self,head):

        bucket = []
        while(head is not None):
            if head in bucket:
                return True
            else:
                bucket.append(head)
            head = head.next
        return False



if __name__ == '__main__':
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)

    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node1

    # head = ListNode(1)
    # node1 = ListNode(2)
    # head.next = node1
    # node1.next = head

    solution = Solution()
    print(solution.hasCycle(head))