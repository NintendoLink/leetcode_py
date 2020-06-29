# python 3.6.4
# encoding: utf-8

from treenode import TreeNode
from queue import Queue
class Solution:
    def isBalanced(self,root):

        return True if not root else abs(self.height(root.left) - self.height(root.right)) <=1


    def height(self,root):
        """
        利用层序遍历求树的高度
        :param root:
        :return:
        """
        count = -1
        if not root:
            return 0

        queue = Queue()
        temp_queue = Queue()
        temp_queue.put(root)


        while (not temp_queue.empty()):

            count +=1
            while (not temp_queue.empty()):
                queue.put(temp_queue.get())

            while (not queue.empty()):
                tempNode = queue.get()

                if tempNode.left:
                    temp_queue.put(tempNode.left)
                if tempNode.right:
                    temp_queue.put(tempNode.right)

        return count


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
    print(solution.height(root.right))
    pass