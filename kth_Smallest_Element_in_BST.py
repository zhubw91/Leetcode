# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        node = root
        stack = []
        while node or len(stack) > 0:
        	if node:
        		stack.append(node)
        		node = node.left
        	else:
        		k -= 1
        		node = stack.pop()
        		if k == 0:
        			return node.val
        		node = node.right