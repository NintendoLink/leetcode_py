# python 3.6.4
# encoding: utf-8
"""
112. 路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from _basestructure.treenode import TreeNode
class Solution:

    """
    思路
    1、递归算法即可
    """
    def hasPathSum(self,root,sum):
        if root is None:
            return False
        return self._hasPathSum(node=root, target=sum)

    def _hasPathSum(self, node:TreeNode, target:int, res=0):

        if node is None:
            return False

        res += node.val

        if node.left is None and node.right is None:
            if res == target:
                return True
            return False

        return self._hasPathSum(node.left, target, res) or self._hasPathSum(node.right, target, res)

if __name__ == '__main__':

    root = TreeNode(10)
    left = TreeNode(5)
    right = TreeNode(15)

    root.left = left
    root.right = right

    right_left = TreeNode(20)
    right_right = TreeNode(7)

    right.left = right_left
    right.right = right_right

    # root = TreeNode(1)
    # left = TreeNode(2)
    # root.left = left
    solution = Solution()
    print(solution.hasPathSum(root, 3))