# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def dfs(self, node, path, depth):
		if depth >= len(path):
			path.append(node.val)
		if node.left == None and node.right == None:
			return path
		if node.right:
			path = self.dfs(node.right, path, depth+1)
		if node.left:
			path = self.dfs(node.left, path, depth+1)
		return path

	def rightSideView(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		path = []
		if root == None:
			return path
		return self.dfs(root, path, 0)
