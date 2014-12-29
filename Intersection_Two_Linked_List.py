# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        p1 = headA
        p2 = headB
        lendif = 0
        if p1 is None or p2 is None:
        	return None
        while p1 != None and p2 != None:
        	if p1 is p2:
        		return p1
        	p1 = p1.next
        	p2 = p2.next       
        if p1 != None:
        	while p1 != None:
        		p1 = p1.next
        		lendif = lendif + 1
        	p3 = headA
        	p4 = headB
        elif p2 != None:
        	while p2 != None:
        		p2 = p2.next
        		lendif = lendif + 1
        	p3 = headB
        	p4 = headA
        else:
        	return None
        while lendif > 0:
        	p3 = p3.next
        	lendif = lendif - 1
        while p3 != None and p4 != None:
        	if p3 is p4:
        		return p3
        	p3 = p3.next
        	p4 = p4.next
        return None


