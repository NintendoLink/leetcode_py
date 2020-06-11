# python 3.6.4
# encoding: utf-8
class ListNode():
    def __init__(self,x):
        self.val = x
        self.next = None

    @staticmethod
    def printall(list):
        while(list):
            print(list.val)
            list = list.next