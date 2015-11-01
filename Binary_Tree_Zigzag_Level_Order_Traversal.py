# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def dfs(self,node,level,result):
		if node == None:
			return 
		if level >= len(result):
			result.append([])
		if level%2 == 0:
			result[level].append(node.val)
		else:
			result[level].insert(0,node.val)
		self.dfs(node.left,level+1,result)
		self.dfs(node.right,level+1,result)

	def zigzagLevelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		result = []
		if root == None:
			return result
		self.dfs(root,0,result)
		return result