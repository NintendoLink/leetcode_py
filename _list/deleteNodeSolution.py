# python 3.6.4
# encoding: utf-8
"""
237. 删除链表中的节点

请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。
示例 1:

输入: head = [4,5,1,9], node = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], node = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
 

说明:

链表至少包含两个节点。
链表中所有节点的值都是唯一的。
给定的节点为非末尾节点并且一定是链表中的一个有效节点。
不要从你的函数中返回任何结果。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-node-in-a-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    """
    一般情况下，删除链表中的节点，需要两个参数：原链表、需要删除的节点，不过题目中只给了一个节点，也即是只给出了被删除的节点，因此可以用替换法去删除
    """
    def deleteNode(self,node):
        node.val = node.next.val
        node.next = node.next.next

if __name__ == '__main__':
    from list import ListNode
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)

    node1.next = node2
    node2.next = node3

    solution = Solution()
    solution.deleteNode(node2)
    while node1:
        print(node1.val)
        node1 = node1.next