# python 3.6.4
# encoding: utf-8
from _basestructure.treenode import TreeNode

class Solution:

    def middle_order(self,root):

        """

        :param root:
        :return:
        """
        return self._pre_order(root)

    def _pre_order(self,root):
        """

        :param root:
        :return:
        """

        stack = []
        while(root is not None or len(stack) > 0):

            if (root is not None):
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                print(node.val)
                root = node.right


        # while(len(stack) > 0):
        #     node = stack.pop()
        #
        #     print(node.val)
        #     if node.right is not None:
        #         stack.append(node.right)
        #     if node.left is not None:
        #         stack.append(node.left)
        #
        #     if node.left is None and node.right is None:
        #         break
if __name__ == '__main__':
    # root = TreeNode(15)
    # left = TreeNode(9)
    # right = TreeNode(21)
    #
    # left_left = TreeNode(7)
    # left_right = TreeNode(13)
    #
    # right_left = TreeNode(19)
    # right_right = TreeNode(23)
    #
    # root.left = left
    # root.right = right
    #
    # left.left = left_left
    # left.right = left_right
    #
    # right.left = right_left
    # right.right = right_right
    #
    # left_left_left = TreeNode(5)
    # left_right_left = TreeNode(12)
    # right_left_left = TreeNode(17)
    #
    # left_left.left = left_left_left
    # left_right.left = left_right_left
    # right_left.left = right_left_left
    # solution = Solution()
    # solution.middle_order(root)

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
    # print(solution.height(root.right))
    print(solution.middle_order(root))