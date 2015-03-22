# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        def recursive(head, n):
            if head is None:
                return None
            p = head
            cnt = 0
            if n == 1:
                return TreeNode(head.val)
            while cnt < n/2:
                p = p.next
                cnt += 1
            if p is None:
                return None
            result = TreeNode(p.val)
            result.left = recursive(head, (n-1)/2)
            result.right = recursive(p.next, n-(n-1)/2)
            return result
        p = head
        n = 0
        if head is None:
            return None
        while p != None:
            p = p.next
            n += 1
        head = recursive(head,n)
        return head
