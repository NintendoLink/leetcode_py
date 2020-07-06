# python 3.6.4
# encoding: utf-8
"""
98. 验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from _basestructure.treenode import TreeNode

class Solution:

    """
    思路
    1、递归，行不通，二叉搜索树的性质是根节点大于左子树下所有的节点，而不是一个节点，因此无法递归
    2、中序遍历存储到线性表中，判断顺序是否是升序
    """
    def isValidBST(self,root:TreeNode):

        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        if root.left is not None and root.val <= root.left.val:
            return False

        if root.right is not None and root.val >= root.right.val:
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)

        # ls_container = []
        # self.middle_order(ls_container,root)
        # for index in range(len(ls_container) - 1):
        #     if ls_container[index + 1] <= ls_container[index]:
        #         return False
        #
        # return True

    def middle_order(self,contrainer,root):

        if root is None:
            return
        self.middle_order(contrainer,root.left)
        contrainer.append(root.val)
        self.middle_order(contrainer,root.right)

if __name__ == '__main__':
    root = TreeNode(10)
    left = TreeNode(5)
    right = TreeNode(15)

    root.left = left
    root.right = right

    solution = Solution()
    print(solution.isValidBST(root))