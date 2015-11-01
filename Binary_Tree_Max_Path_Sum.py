# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def dfs(self,node):
		global_max = node.val
		local_max = node.val
		left_max = node.val
		right_max = node.val
		if node.left:
			left_max,tmp = self.dfs(node.left)
			local_max = max(local_max,left_max+node.val)
			global_max = max(tmp,global_max)
		else:
			left_max = 0
		if node.right:
			right_max,tmp = self.dfs(node.right)
			local_max = max(local_max,right_max+node.val)
			global_max = max(tmp,global_max)
		else:
			right_max = 0

		global_max = max(local_max,global_max,left_max+node.val+right_max)
		return local_max,global_max

	def maxPathSum(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if root == None:
			return 0
		return self.dfs(root)[1]
