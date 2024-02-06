# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p1 = head
        if (p1 != None):
            p2 = head.next
            while p1 != None:
                if (p1 == p2):
                    return True
                elif (p2 == None):
                    return False
                if (p2.next != None):
                    p1 = p1.next
                    p2 = p2.next.next
                else:
                    return False
        return False