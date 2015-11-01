# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def upsideDownBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		stack = []
		if root == None:
			return None
		node = root
		while node != None:
			stack.append(node)
			node = node.left
		head = stack[-1]
		l = len(stack)
		while l > 1:
			node = stack[l-1]
			node.right = stack[l-2]
			node.left = stack[l-2].right
			l -= 1
		stack[0].left = stack[0].right = None
		return head
