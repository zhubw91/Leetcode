# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
	def hasCycle(self, head):
		fast = head
		slow = head
		if fast is None:
			return False
		while True:
			fast = fast.next
			if fast is None:
				return False
			if fast is slow:
				return True
			fast = fast.next
			if fast is None:
				return False
			if fast is slow:
				return True
			slow = slow.next