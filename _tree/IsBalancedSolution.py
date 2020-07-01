# python 3.6.4
# encoding: utf-8

"""
面试题 04.04. 检查平衡性

实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。


示例 1:
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。
示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]
      1
     / \
    2   2
   / \
  3   3
 / \
4   4
返回 false 。
"""
from treenode import TreeNode
from queue import Queue
class Solution:
    """
    思路：
        如果一棵二叉树是平衡树，则有：
            每个节点的左右子树的深度之差不超过1
            每个节点的左右子树分别是二叉平衡树
        根据树的性质，递归的求解

    """
    def isBalanced(self,root):

        if root is None:
            return True
        if (abs(self.maxDepth(root.left) - self.maxDepth(root.right)) >1):
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    # 广度优先搜索求二叉树的深度
    def maxDepth(self,root):
        if root is None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1

    # # 二叉树求深度的算法，利用深度优先搜索
    # def maxDepth(self, root):
    #     """
    #     利用层序遍历求树的高度
    #     :param root:
    #     :return:
    #     """
    #     count = 0
    #     if not root:
    #         return 0
    #
    #     queue = Queue()
    #     temp_queue = Queue()
    #     temp_queue.put(root)
    #
    #     while (not temp_queue.empty()):
    #
    #         count +=1
    #         while (not temp_queue.empty()):
    #             queue.put(temp_queue.get())
    #
    #         while (not queue.empty()):
    #             tempNode = queue.get()
    #
    #             if tempNode.left:
    #                 temp_queue.put(tempNode.left)
    #             if tempNode.right:
    #                 temp_queue.put(tempNode.right)
    #
    #     return count


if __name__ == '__main__':
    root = TreeNode(3)

    firstleft = TreeNode(9)
    firstright = TreeNode(20)

    root.left = firstleft
    root.right = firstright

    secondleft = TreeNode(15)
    secondrigth = TreeNode(7)

    firstright.left = secondleft
    firstright.right = secondrigth

    solution = Solution()
    # print(solution.height(root.right))
    print(solution.isBalanced(root))
    pass