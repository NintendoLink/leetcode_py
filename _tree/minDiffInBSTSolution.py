# python 3.6.4
# encoding: utf-8
"""
783. 二叉搜索树节点最小距离
给定一个二叉搜索树的根节点 root，返回树中任意两节点的差的最小值。

 

示例：

输入: root = [4,2,6,1,3,null,null]
输出: 1
解释:
注意，root是树节点对象(TreeNode object)，而不是数组。

给定的树 [4,2,6,1,3,null,null] 可表示为下图:

          4
        /   \
      2      6
     / \
    1   3

最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from _basestructure.treenode import TreeNode
class Solution:

    """
    思路：刚开始以为：最小值必然在根节点与直系孩子节点产生，通不过测试用例，错误[90,69,null,49,89,null,52,null,null,null,null]
    1、中序递归算法
    2、将数据中序遍历后保存到线性集合众，然后找最小值
    """

    def minDiffInBST(self, root):
        def dfs(node):
            if node:
                dfs(node.left)
                self.ans = min(self.ans, node.val - self.prev)
                self.prev = node.val
                dfs(node.right)

        self.prev = float('-inf')
        self.ans = float('inf')
        dfs(root)
        return self.ans

    # 错误代码
    # def minDiffInBST(self,root):
    #     return self._minDiffInBST(root)
    #
    # def _minDiffInBST(self, root):
    #
    #     # 节点的的最小差值初始化为999，空节点也初始化为999
    #     if root is None:
    #         return 999
    #
    #     current_min = 999
    #     child_min = min(self._minDiffInBST(root.left),self._minDiffInBST(root.right))
    #
    #     if root.left is not None:
    #         current_min = current_min if current_min < root.val - root.left.val else root.val - root.left.val
    #
    #     if root.right is not None:
    #         current_min = current_min if current_min < root.right.val - root.val else root.right.val - root.val
    #
    #     return current_min if current_min < child_min else child_min

if __name__ == '__main__':
    root = TreeNode(15)
    left = TreeNode(9)
    right = TreeNode(21)

    left_left = TreeNode(7)
    left_right = TreeNode(13)

    right_left = TreeNode(19)
    right_right = TreeNode(23)

    root.left = left
    root.right = right

    left.left = left_left
    left.right = left_right

    right.left = right_left
    right.right = right_right

    left_left_left = TreeNode(5)
    left_right_left = TreeNode(12)
    right_left_left = TreeNode(17)

    left_left.left = left_left_left
    left_right.left = left_right_left
    right_left.left = right_left_left
    solution = Solution()
    print(solution.minDiffInBST(root))