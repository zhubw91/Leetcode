# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
        	return head
        p = None
        q = head
        r = head.next
        while q:
        	q.next = p
        	p = q
        	q = r
        	if r:
        		r = r.next
        return p
        