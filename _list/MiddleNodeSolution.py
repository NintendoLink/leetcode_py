# python 3.6.4
# encoding: utf-8
from list import ListNode

"""
876. 链表的中间结点

给定一个带有头结点 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

 

示例 1：

输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
示例 2：

输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/middle-of-the-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:

    """
    思路：
    1、快慢指针
    """
    def middleNode(self,head):

        slow_pivot = ListNode(None)
        fast_pivot = ListNode(None)

        fast_pivot.next = head
        slow_pivot.next = head

        while(fast_pivot):
            if(fast_pivot.next):
                slow_pivot = slow_pivot.next
                fast_pivot = fast_pivot.next.next
            else:
                break
        if (fast_pivot):
            return slow_pivot.next
        else:
            return slow_pivot

if __name__ == '__main__':

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5


    # ListNode.printall(head)
    solution = Solution()
    # print(solution.middleNode(head).val)
    ListNode.printall(solution.middleNode(node1))