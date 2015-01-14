# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
    	current = head = ListNode(0)
    	lists = [(i.val,i) for i in lists if i]
    	heapq.heapify(lists)
    	while lists:
    		current.next = heapq.heappop(lists)[1]
    		current = current.next
    		if current.next:
    			heapq.heappush(lists, (current.next.val, current.next))
    	return head.next
