__author__ = 'Muming'
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        if head is None:
            return None
        temp = head
        while temp is not None:
            if temp.next is not None:
                rtemp = temp.next
            if rtemp.val == val:
                temp.next = rtemp.next
                rtemp.next = None
            temp = temp.next
        if head.val == val:
            return head.next
        else:
            return head

def test():
    st = Solution()
    head = ListNode(1)
    # head.next = ListNode(1)
    print st.removeElements(head, 1)


if __name__ == '__main__':
    test()
    pass