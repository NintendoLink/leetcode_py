# python 3.6.4
# encoding: utf-8
class TreeNode:
    """
    二叉树
    """
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Node:
    """
    多叉树
    """
    def __init__(self,val = None,children = None):
        self.val = val
        self.children = children