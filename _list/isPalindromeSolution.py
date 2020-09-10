# python 3.6.4
# encoding: utf-8
"""
234. 回文链表
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
"""
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:

    """
    思路1
    1、常规解法即可
    """
    def isPalindrome(self, head:ListNode):

        if head is None:
            return True
        if head.next is None:
            return True

        container = []

        while(head):
            container.append(head.val)
            head = head.next

        right_point = (len(container) + 1) // 2
        left_point = (len(container) // 2) - 1

        while(left_point >= 0):
            if container[left_point] == container[right_point]:
                return False
            left_point -= 1
            right_point += 1

        return True

if __name__ == '__main__':


    solution = Solution()

    head = ListNode(-129)
    head.next = ListNode(-129)
    # head.next.next = ListNode(2)
    # head.next.next.next = ListNode(1)
    print(solution.isPalindrome(head))

    # container = [1,3,4,5,5,6,7]
    # right_point = (len(container) + 1) // 2
    # left_point = (len(container) // 2) - 1
    #
    # print("left:{},right:{}".format(left_point,right_point))