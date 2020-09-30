
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
"""
206. 反转链表

反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
class Solution:


    """
    思路
    1、利用其他容器将数据先全部取出来，在生成新的链表
    2、利用前后指针直接修该链表中next的指向
    """
    # 1 --->>> 2 --->>> 3 --->>>None
    def reverseList(self,head:ListNode):

        pre = head
        next = head.next
        head.next = None
        while(next):
            temp = next.next
            next.next = pre
            pre = next
            next = temp

        return pre

    def reverseList2(self, head:ListNode):

        temp_container = []
        while(head):
            temp_container.append(head.val)
            head = head.next

        result_node = ListNode(0)
        result_head = result_node

        for i in range(len(temp_container) - 1,-1,-1):
            result_node.next = ListNode(temp_container[i])
            result_node = result_node.next

        return result_head.next

if __name__ == '__main__':

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)

    # node1.next = node2
    # node2.next = node3

    solution = Solution()
    reverse_node = solution.reverseList(node1)

    while(reverse_node):
        print(reverse_node.val)
        reverse_node = reverse_node.next