# python 3.6.4
# encoding: utf-8
"""
剑指 Offer 68 - I. 二叉搜索树的最近公共祖先
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]



 

示例 1:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from _basestructure.treenode import TreeNode
class Solution:

    def lowestCommonAncestor(self,root:TreeNode,p:TreeNode,q:TreeNode):

        """
        思路，注意说明:所有节点的值都是唯一的。p、q 为不同节点且均存在于给定的二叉搜索树中。
        根据二叉搜索树的性质，如果是最近公共祖先，那么一定是大于一个小于另外一个，如果等于其中一个，则返回即可
        因此可以有迭代法和递归法
        :param root:
        :param p:
        :param q:
        :return:
        """

        # 迭代法
        if p.val > q.val:
            temp = q
            q = p
            p = temp

        while root:
            # 如果根节点大于最大值，则一定在左子树当中
            if root.val > q.val:
                root = root.left
            # 如果根节点小于最小值，则一定在右子树当中
            elif root.val < p.val:

                # 其他情况则直接返回
                root = root.right
            else:
                break
        return root


        # 递归法
        # if root is None:
        #     return None
        #
        # if root.val > p.val and root.val > q.val:
        #     return self.lowestCommonAncestor(root.left,p,q)
        #
        # if root.val < p.val and root.val < q.val:
        #     return self.lowestCommonAncestor(root.right,p,q)
        #
        # return root

if __name__ == '__main__':

    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right

    right_left = TreeNode(4)
    right_right = TreeNode(5)

    right.right = right_right
    right.left = right_left

    solution = Solution()
    print(solution.lowestCommonAncestor(None,None,None))