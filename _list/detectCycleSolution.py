# python 3.6.4
# encoding: utf-8
"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from _basestructure.list import ListNode
class Solution:
    """
    本题是要将环形的入口节点返回，是判断是否存在环的升级
    思路1：利用hash算法，将list中的数据存储在哈希表中，如果遇到相同元素，则返回
    思路2：利用快慢指针，在第一次相遇之后，将快指针移到head节点，则第二次相遇一定在环形入口节点
    """

    # # 思路1
    # def detectCycle(self,head):
    #     bucket = []
    #     while(head is not None):
    #         if head in bucket:
    #             return head
    #         else:
    #             bucket.append(head)
    #         head = head.next
    #     return None

    # 双指针法
    def detectCycle(self,head):

        if (not head or not head.next or not head.next.next):
            return
        fast = head.next.next
        slow = head.next

        while(True):
            if (fast is None or fast.next is None):
                return
            if (slow == fast):
                break
            fast = fast.next.next
            slow = slow.next
        fast = head
        while(fast is not slow):
            fast = fast.next
            slow = slow.next

        return fast
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
    #
    # head.next = node1
    # node1.next = head
    solution = Solution()
    print(solution.detectCycle(head).val)