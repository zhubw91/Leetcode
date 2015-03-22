# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None:
        	return None
        fast = head.next
        slow = head
        slowval = 0
        fastval = 1
        while fast != None and fast != slow:
        	fast = fast.next
        	slow = slow.next
        	slowval += 1
        	fastval += 1
        	if fast != None:
        		fast = fast.next
        		fastval += 1
        if fast == None:
        	return None
        l = fastval - slowval
        fast = head
        while l > 0:
        	fast = fast.next
        	l -= 1
        slow = head
        while slow != fast:
        	slow = slow.next
        	fast = fast.next
        return slow




        
        