# python 3.6.4
# encoding: utf-8

from _basestructure.treenode import TreeNode
class BSTree:

    def __init__(self):
        self.root = None

    def build_from_list(self,ls:list):

        for ele in ls:
            self.insert(ele)

        return

    def insert(self,value):
        if self.root is None:
            self.root = TreeNode(value)
            return
        node = self.root
        self._insert(node,value)

    def _insert(self,root,value):
        """
        递归的插入元素
        :param root:
        :param value:
        :return:
        """
        if root is None:
            return TreeNode(value)
        if root.val > value:
            root.left = self._insert(root.left,value)
        elif root.val < value:
            root.right = self._insert(root.right,value)
        else:
            return None
        return root

    def search(self,obj):
        node = self.root
        return self._search(node,obj)

    def _search(self, node, obj):
        """
        递归查找元素
        :param node:
        :param obj:
        :return:
        """
        if node is None:
            return None
        if node.val == obj:
            return node
        elif node.val > obj:
            return self._search(node.right, obj)
        else:
            return self._search(node.left,obj)

    @staticmethod
    def middle_order(node):
        if node is None:
            return
        BSTree.middle_order(node.left)
        print(node.val)
        BSTree.middle_order(node.right)

if __name__ == '__main__':
    ls = [1,2,3]
    bstree = BSTree()
    bstree.build_from_list(ls)
    BSTree.middle_order(bstree.root)
    print(bstree.search(10).val)
