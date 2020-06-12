# python 3.6.4
# encoding: utf-8

"""
102. 二叉树的层序遍历

给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from queue import Queue
from treenode import TreeNode
class Solution:

    def levelOrder(self,root):
        """
        第二种写法，使用双队列，输出的为[[3],[9,20],[15,7]]，这种写法可以引申出求一棵树的高度。
        :param root:
        :return:
        """
        if not root:
            return []
        queue = Queue()
        temp_queue = Queue()
        temp_queue.put(root)
        res = []

        while(not temp_queue.empty()):

            while(not temp_queue.empty()):
                queue.put(temp_queue.get())

            temp_res = []
            while(not queue.empty()):
                tempNode = queue.get()

                temp_res.append(tempNode.val)

                if tempNode.left:
                    temp_queue.put(tempNode.left)
                if tempNode.right:
                    temp_queue.put(tempNode.right)

            res.append(temp_res)
        return res

    # def levelOrder(self,root):
    #     """
    #     这个版本的输出结果为：[3,9,20,15,7]
    #     :param root:
    #     :return:
    #     """
    #     if not root:
    #         return []
    #     queue = Queue()
    #     queue.put(root)
    #     res = []
    #
    #     while(not queue.empty()):
    #         tempNode = queue.get()
    #         res.append(tempNode.val)
    #
    #         if tempNode.left:
    #             queue.put(tempNode.left)
    #         if tempNode.right:
    #             queue.put(tempNode.right)
    #     return res

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
    solution.levelOrder(root)

    pass