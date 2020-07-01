# python 3.6.4
# encoding: utf-8

"""
101. 对称二叉树

给定一个二叉树，检查它是否是镜像对称的。



例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3


但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3


进阶：

你可以运用递归和迭代两种方法解决这个问题吗？
"""
from _basestructure.treenode import TreeNode
from queue import Queue

class Solution:

    """
    思路：
    1、迭代算法：利用广度优先搜索遍历，二叉树的层序遍历，双队列
    3、递归算法
    """
    # 思路1
    # def isSymmetric(self,root):
    #     queue = Queue()
    #     # 为了防止父节点get之后为空，得不到原来的父节点，采用另外的队列进行存储
    #     temp_queue = Queue()
    #     # 父节点队列
    #     queue.put(root)
    #     while(not queue.empty()):
    #         # 将父节点中的数据倒腾到temp_queue中
    #         while(not queue.empty()):
    #             node = queue.get()
    #             temp_queue.put(node)
    #         if not self._isDualQueue(temp_queue):
    #             return False
    #
    #         while(not temp_queue.empty()):
    #             node = temp_queue.get()
    #             if node is not None:
    #                 queue.put(node.left)
    #                 queue.put(node.right)
    #     return True


    def _isDualQueue(self,queue):

        for index in range(0,int(len(queue.queue)/2)):
            # 1、首先是非空情况：两个都不为空(反面情况：有一个为空)
            if (queue.queue[index] is not None and queue.queue[len(queue.queue) - index - 1] is not None):
                if queue.queue[index].val != queue.queue[len(queue.queue) - index - 1].val:
                # if stack[index] != stack[len(stack) - index - 1]:
                    return False
            else:
            # 2、如果有一个为空，则两个必须都为空，否则返回Fasle
                if not (queue.queue[index] is None and queue.queue[len(queue.queue) - index - 1] is None):
                    return False
        return len(queue.queue) % 2 == 0 or len(queue.queue) == 1


    # 递归算法
    def isSymmetric(self,root):

        return self.check(root.left,root.right)

    def check(self,nodeP,nodeQ):
        # 两个都不为空
        if nodeP is None and nodeQ is None:
            return True
        # 两个有且只有一个为空
        if nodeP is None or nodeQ is None:
            return False
        return nodeP.val == nodeQ.val and \
                self.check(nodeP.left,nodeQ.right) and \
                self.check(nodeP.right,nodeQ.left)


if __name__ == '__main__':
    root = TreeNode(1)
    root_left = TreeNode(2)
    root_right = TreeNode(2)
    root_left_left = TreeNode(3)
    root_left_right = TreeNode(5)
    root_right_left = TreeNode(4)
    root_right_right = TreeNode(3)

    root.left = root_left
    root.right = root_right

    root_left.left = root_left_left
    root_left.right = root_left_right
    root_right.left = root_right_left
    root_right.right = root_right_right
    # ls = [1,None,3,4,3,None,1]
    solution = Solution()
    print(solution.isSymmetric(root))
    # print(solution._isDualQueue(None,ls))
