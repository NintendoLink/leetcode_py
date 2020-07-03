# Definition for a binary tree node.
"""
173. 二叉搜索树迭代器

实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。

调用 next() 将返回二叉搜索树中的下一个最小的数。

示例：


BSTIterator iterator = new BSTIterator(root);
iterator.next();    // 返回 3
iterator.next();    // 返回 7
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 9
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 15
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 20
iterator.hasNext(); // 返回 false
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    """
    思路
    1、二叉树的升序也即是按照中序遍历二叉树，所以将数据全部保存到list container中
    2、可控的中序遍历递归
    """
    def __init__(self, root: TreeNode):
        self._ls_container = []
        self._middle(root,self._ls_container)
        self._pointer = 0


    def next(self) -> int:
        """
        @return the next smallest number
        """
        self._pointer += 1
        return self._ls_container[self._pointer - 1]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self._pointer != len(self._ls_container)


    def _middle(self,node:TreeNode,ls:list):
        if node is None:
            return
        self._middle(node.left,ls)
        ls.append(node.val)
        self._middle(node.right,ls)
if __name__ == '__main__':

    root = TreeNode(7)
    left = TreeNode(3)
    right = TreeNode(15)
    right_left = TreeNode(9)
    right_right = TreeNode(20)

    root.left = left
    root.right = right

    right.left = right_left
    right.right= right_right

    bsiter = BSTIterator(root)

    while(bsiter.hasNext()):
        print(bsiter.next())
