# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def find(self, node):
		if node.left == None and node.right == None:
			return [True, node.val, 1]
		if node.left:
			result_left = self.find(node.left)
		else:
			result_left = [True, node.val, 0]
		if node.right:
			result_right = self.find(node.right)
		else:
			result_right = [True, node.val, 0]
		if result_left[0] and result_right[0] and result_right[1]==result_left[1] and result_left[1] == node.val:
			return [True, node.val, result_left[2]+result_right[2]+1]
		else:
			return [False, 0, result_right[2]+result_left[2]]
	def countUnivalSubtrees(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if root == None:
			return 0
		else:
			result = self.find(root)
			return result[2]