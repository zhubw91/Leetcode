# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        p1 = l1
        p2 = l2
        result = ListNode(0)
        q = result
        if p1 == None and p2 == None:
        	return 0
        r = 0
        while p1 != None or p2 != None:
        	if p1 == None:
        		x = 0
        	else:
        		x = p1.val
        		p1 = p1.next
        	if p2 == None:
        		y = 0
        	else:
        		y = p2.val
        		p2 = p2.next
        	q.next = ListNode((x+y+r)%10)
        	q = q.next
        	r = (x + y + r)/10
        if r > 0:
        	q.next = ListNode(r)
        return result.next

