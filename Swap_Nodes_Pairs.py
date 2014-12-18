# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        p = head
        q = None
        while p!= None and p.next != None:
        	if q != None:
        		q.next = p.next
        	else:
        		head = p.next
        	r = p.next
        	p.next = r.next
        	r.next = p
        	q = p
        	p = p.next
        return head