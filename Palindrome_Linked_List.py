# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = head
        if head == None:
        	return False
        l = 0
        while p:
        	p = p.next
        	l += 1
        p = head
        count = 1
        while p and count < (l+1)/2:
        	p = p.next
        	count += 1
        q = p.next
        r = q.next
        while r:
        	q.next = p
        	p = r
        	r = r.next
        q.next = p
        p = head
        while p!=q and p.next!=q.next:
        	if p.val != q.val:
        		return False
        	p = p.next
        	q = q.next


