# python 3.6.4
# encoding: utf-8
"""
100. 相同的树

给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]
"""
from _basestructure.treenode import TreeNode
class Solution:

    """
    注意递归结束的条件
    在树的递归中，不直接判断父节点所要满足为正的条件，而判断为负的条件，因为直接条件不满足d
    """
    def isSameTree(self,root1,root2):

        if root1 is None and root2 is None:
            return True

        if root1 is not None and root2 is not None:
            if root1.val != root2.val:
                return False

        if root1 is None and root2 is not None:
            return False

        if root2 is None and root1 is not None:
            return False

        return self.isSameTree(root1.left, root2.left) and \
               self.isSameTree(root1.right, root2.right)
if __name__ == '__main__':
    root1 = TreeNode(10)
    left = TreeNode(5)
    right = TreeNode(15)

    root1.left = left
    root1.right = right

    root2 = root1
    solution = Solution()
    print(solution.isSameTree(root1, root2))