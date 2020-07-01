# python 3.6.4
# encoding: utf-8
"""
剑指 Offer 55 - I. 二叉树的深度
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from _basestructure.treenode import TreeNode
from queue import Queue

class Solution:

    """
    思路
    1、根据层序遍历来求树的深度
    2、递归的求树的深度
    """
    # # 思路1、利用层序遍历
    # def maxDepth(self,root):
    #
    #     if (not root):
    #         return
    #
    #     temp_queue = Queue()
    #     queue = Queue()
    #     queue.put(root)
    #     res = []
    #     count = 0
    #     while(not queue.empty()):
    #         ls = []
    #         while(not queue.empty()):
    #
    #             node = queue.get()
    #             ls.append(node.val)
    #             temp_queue.put(node)
    #         res.append(ls)
    #         count += 1
    #         while(not temp_queue.empty()):
    #             node = temp_queue.get()
    #             if (node.left is not None):
    #                 queue.put(node.left)
    #             if (node.right is not None):
    #                 queue.put(node.right)
    #
    #     return count
    def maxDepth(self,root):
        if root is None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1
if __name__ == '__main__':
    root = TreeNode(3)
    root_left = TreeNode(9)
    root_right = TreeNode(20)

    root.left = root_left
    root.right = root_right

    root_right_left = TreeNode(15)
    root_right_right = TreeNode(7)

    root_right.left = root_right_left
    root_right.right = root_right_right

    solution = Solution()
    print(solution.maxDepth(root))