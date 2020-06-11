# python 3.6.4
# encoding: utf-8
from list import ListNode
class Solution:
    def deleteDuplicates(self,head):

        pivot1 = head
        pivot2 = head
        while(pivot1):
            if (pivot2.next is not None) & (pivot2.val == pivot2.next.val):
                temp = pivot2.val
                while(pivot2):
                    if pivot2.val!= temp:
                        break
                    else:
                        pivot2 = pivot2.next
                if(pivot2):
                    pivot1.next = pivot2
                    pivot1 = pivot2
                    continue
            pivot1 = pivot1.next
            pivot2 = pivot2.next
        return head
if __name__ == '__main__':

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(3)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    solution = Solution()
    # ListNode.printall(node1)
    ListNode.printall(solution.deleteDuplicates(node1))