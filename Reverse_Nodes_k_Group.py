# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if k <= 1:
        	return head
        p = head
        q = head
        l = 0
        while q != None:
        	l += 1
        	q = q.next
        n = l/k
        q = head
        for i in range(n):
        	p = q
        	h = p
        	t = q.next
        	for j in range(k-1):
        		p = q
        		q = t
        		t = q.next
        		q.next = p
        	if i == 0:
        		head = q
        	else:
        		r.next = q
        	h.next = t
        	r = h
        	q = t
        return head
