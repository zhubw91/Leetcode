# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        watcher = ListNode(0)
        watcher.next = head
        p = watcher
        while p.next and p.next.next:
        	if p.next.val == p.next.next.val:
        		q = p.next.next.next
        		while q and p.next.val == q.val:
        			q = q.next
        		p.next = q
        	else:
        		p = p.next
        return watcher.next