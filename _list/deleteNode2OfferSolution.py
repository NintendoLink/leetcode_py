class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

"""
剑指 Offer 18. 删除链表的节点
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:

输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
 

说明：

题目保证链表中节点的值互不相同
若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
class Solution:

    """
    思路
    1、需要注意的删除最后一个节点，如果没有头指针，是不能置空的，因此，需要在链表头部加上一个头指针
    """
    def deleteNode(self,head:ListNode,val:int):

        ls_head = ListNode(0)
        ls_head.next = head
        ls_head_copy = ls_head
        while(ls_head.next):

            if ls_head.next.val == val:
                ls_head.next = ls_head.next.next
                return ls_head_copy.next

            ls_head = ls_head.next

        return ls_head_copy.next

if __name__ == '__main__':
    solution = Solution()

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    val = 4

    node = solution.deleteNode(node1,2)
    while(node):
        print(node.val)
        node = node.next