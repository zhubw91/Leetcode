# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
    	head = None
    	p = None
    	while l1 != None and l2 != None:
    		if l1.val < l2.val:
    			if head is None:
    				head = l1
    				p = head
    			else:
    				p.next = l1
    				p = l1
    			l1 = l1.next
    		else:
    			if head is None:
    				head = l2
    				p = head
    			else:
    				p.next = l2
    				p = l2
    			l2 = l2.next
    	if l1 != None:
    		if p is None:
    			head = l1
    		else:
    			p.next = l1
    	if l2 != None:
    		if p is None:
    			head = l2
    		else:
    			p.next = l2
    	return head
