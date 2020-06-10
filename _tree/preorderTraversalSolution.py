# python 3.6.4
# encoding: utf-8
from treenode import TreeNode
"""
144. 二叉树的前序遍历
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""
class Solution:
    # 递归算法
    # def preorderTraversal(self,root):
    #     container = []
    #     self._preorderTraversal(root=root,container=container)
    #     return container
    # def _preorderTraversal(self,root,container):
    #
    #     if root is None:
    #         return
    #     else:
    #         container.append(root.val)
    #         self._preorderTraversal(root.left,container)
    #         self._preorderTraversal(root.right,container)

    # 非递归算法，方法1
    def preorderTraversal(self, root):
        res = []
        if root is None:
            return res

        stack = []
        stack.append(root)

        while(len(stack) > 0):
            current_node = stack.pop()
            res.append(current_node.val)

            if current_node.right is not None:
                stack.append(current_node.right)
            if current_node.left is not None:
                stack.append(current_node.left)
        return res


if __name__ == '__main__':

    from treenode import TreeNode

    root = TreeNode(val=1)
    root.right = TreeNode(val=2)
    root.right.left = TreeNode(val=3)

    solution = Solution()
    print(solution.preorderTraversal(root))
    pass