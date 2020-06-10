# python 3.6.4
# encoding: utf-8
"""
145. 二叉树的后序遍历
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    # # 递归算法
    # def postorderTraversal(self,root):
    #     res = []
    #     self._postorderTraversal(res,root)
    #     return res
    #
    # def _postorderTraversal(self,res,root):
    #     if not root:
    #         return
    #     self._postorderTraversal(res,root.left)
    #     self._postorderTraversal(res,root.right)
    #     res.append(root.val)

    # 和前序遍历同样思路的迭代算法，第一种迭代方法
    def postorderTraversal(self,root):
        res = []
        if not root:
            return res

        stack = [root]
        while(len(stack) > 0):
            temp = stack.pop()
            res.append(temp.val)
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
        return list(reversed(res))

if __name__ == '__main__':
    from treenode import TreeNode

    root = TreeNode(val=1)
    root.right = TreeNode(val=2)
    root.right.left = TreeNode(val=3)

    solution = Solution()
    print(solution.postorderTraversal(root))