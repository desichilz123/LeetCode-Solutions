# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list2:
            return list1
        elif not list1:
            return list2
        else:
            if list1.val < list2.val:
                return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
            return  ListNode(list2.val, self.mergeTwoLists(list2.next, list1))