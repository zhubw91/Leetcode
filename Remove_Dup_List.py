# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
        	return head
        else:
        	last = head
        	p = head
        	while p != None:
        		if p.val != last.val:
        			last.next = p
        			last = p
        		p = p.next
        	last.next = None
        return head