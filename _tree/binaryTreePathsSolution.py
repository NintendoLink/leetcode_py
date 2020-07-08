# python 3.6.4
# encoding: utf-8
"""
257. 二叉树的所有路径
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import copy
from _basestructure.treenode import TreeNode
class Solution:

    """
    思路
    1、递归算法
    """
    def binaryTreePaths(self,root):

        temp = ""
        res = []
        if root is None:
            return res
        return self._binaryTreePaths(root,res,temp)

    def _binaryTreePaths(self,root:TreeNode,res:list,temp:str):

        if root.left is None and root.right is None:
            cpy_str = copy.deepcopy(temp)
            cpy_str = cpy_str + str(root.val)
            res.append(cpy_str)
            return res

        temp = temp + str(root.val) + "->"

        if root.left is not None:
            self._binaryTreePaths(root.left,res,temp)
        if root.right is not None:
            self._binaryTreePaths(root.right,res,temp)

        return res

    # def _binaryTreePaths(self,root:TreeNode,res:list,temp:list):
    #
    #     if root.left is None and root.right is None:
    #         cpy_list = copy.deepcopy(temp)
    #         cpy_list.append(root.val)
    #         res.append(cpy_list)
    #         return res
    #
    #     temp.append(root.val)
    #
    #     if root.left is not None:
    #         self._binaryTreePaths(root.left,res,temp)
    #     if root.right is not None:
    #         self._binaryTreePaths(root.right,res,temp)
    #
    #     return res
if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right

    left.left = TreeNode(10)
    right_left = TreeNode(4)
    right_right = TreeNode(5)

    right.right = right_right
    right.left = right_left

    solution = Solution()
    print(solution.binaryTreePaths(root))