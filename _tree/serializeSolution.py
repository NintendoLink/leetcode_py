# Definition for a binary tree node.
"""
297. 二叉树的序列化与反序列化
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from queue import Queue
class Codec:

    """
    思路：
        序列化
            比较好解决，只需按照层序遍历即可
        反序列化
            data字符串所表示的并不是一棵完全二叉树，因此利用完全二叉树去反序列化的思路行不通
    """

    def serialize(self, root):
        """Encodes a tree to a single string.
        层序遍历序列化所给的树
        :type root: TreeNode
        :rtype: str
        """
        queue = Queue()
        queue.put(root)

        container = []
        while(not queue.empty()):

            node = queue.get()

            if node is None:
                container.append(node)
                continue
            else:
                container.append(node.val)

            queue.put(node.left)
            queue.put(node.right)
        res = "["
        last_index = len(container) - 1

        if last_index < 0:
            return None
        while(container[last_index] is None):
            last_index -= 1

        for index in range(0,last_index):
            res += str(container[index]) + ","

        res += str(container[last_index]) + "]"
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        这部分代码是对于一棵完全二叉树进行的反序列化
        :type data: str
        :rtype: TreeNode
        """

        if data is None:
            return None
        data = data.replace("]", "")
        data = data.replace("[", "")
        strNun = data.split(",")

        lineTree = []
        # for str in strNun:
        #     if str != 'None':
        #         lineTree.append(int(str))
        #     else:
        #         lineTree.append(None)

        for str in strNun:
            if str != 'None':
                lineTree.append(TreeNode(int(str)))
            else:
                lineTree.append(None)
        #(len(lineTree)-1)/2 向下取整 在广度遍历中最后一个含有子节点的节点，也即是最后一个非叶子节点
        startIndex= (len(lineTree)) // 2 - 1

        for i in range(0,startIndex + 1):
            if lineTree[i] is None:
                continue
            lineTree[i].left = lineTree[2 * i +1]
            if (2 * i + 2) < len(lineTree):
                lineTree[i].right = lineTree[2 * i +2]

        root = lineTree[0]
        return root
        # self.pre_order(root)

    def pre_order(self,root):

        if root is None:
            return
        print(root.val)
        self.pre_order(root.left)
        self.pre_order(root.right)


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

    solution = Codec()
    print(solution.serialize(root))

    # solution = Codec()
    # # data = "[1,2,3,None,None,4,5,None,None,None,None,6,7,8,9]"
    # data = "[1,2,3,None,None,4,5]"
    # print(solution.deserialize(data))
