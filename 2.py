# -*- coding:utf-8 -*-
import math

__author__ = 'Muming'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        mod = 0
        root = ListNode(0)
        upnode = root
        while l1 or l2 or mod:
            v1 = 0
            v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            mod, val = divmod(v1 + v2 + mod, 10)

            node = ListNode(val)
            upnode.next = node
            upnode = node
        return root.next



def print_node(node_root):
    pnode = node_root
    while True:
        print pnode.val
        if pnode.next is None:
            break
        else:
            pnode = pnode.next







def test():
    l1 = ListNode(5)
    l11 = ListNode(6)
    l111 = ListNode(7)

    l2 = ListNode(4)
    l22 = ListNode(5)
    l222 = ListNode(6)
    l2222 = ListNode(7)


    l1.next = l11
    l11.next = l111
    l2.next = l22
    l22.next = l222
    l222.next = l2222

    l2 = [0]
    l1 = [0]
    atn = Solution()
    atn.addTwoNumbers(l1, l2)

if __name__ == '__main__':
    test()

    pass