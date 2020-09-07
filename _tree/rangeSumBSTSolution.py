# python 3.6.4
# encoding: utf-8
"""
938. 二叉搜索树的范围和给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。

二叉搜索树保证具有唯一的值。

 

示例 1：

输入：root = [10,5,15,3,7,null,18], L = 7, R = 15
输出：32
示例 2：

输入：root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
输出：23

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-of-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from _basestructure.treenode import TreeNode
class Solution:

    """
    思路：提干的意思是找到在范围内(int值，并不是节点)的所有节点
    1、中序遍历递归，将tree中的数据线性表示
    """
    def rangeSumBST(self,root,L,R):

        if root is None:
            return None
        container = []
        self._middle_order(root, container)

        index = 0
        res = 0
        while(index <= len(container) - 1 and container[index] < L ):
            index += 1

        while(index <= len(container) - 1 and container[index] <= R ):
            res += container[index]
            index += 1

        return res

    def _middle_order(self, root, container):

        if root is None:
            return
        self._middle_order(root.left, container)
        container.append(root.val)
        self._middle_order(root.right, container)


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
    left_right_left = TreeNode(11)
    right_left_left = TreeNode(17)

    left_left.left = left_left_left
    left_right.left = left_right_left
    right_left.left = right_left_left
    solution = Solution()
    print(solution.rangeSumBST(root,21,23))