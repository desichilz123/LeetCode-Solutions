class Solution(object):
    nodeCnt = 0
    sum = 0
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            self.sum = -1
        else:
            self.nodeCnt += 1 
            self.removeNthFromEnd(head.next, n)
            self.sum += 1
            if self.sum == n:
                head.next = head.next.next
            elif self.sum == (self.nodeCnt - 1) and self.nodeCnt == n:
                head = head.next
            print(self.sum)
            return head