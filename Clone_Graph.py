# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution(object):
	def dfs(self,node,new_node,visited):
		for neighbor in node.neighbors:
			if neighbor.label not in visited:
				next_node = UndirectedGraphNode(neighbor.label)
				visited[neighbor.label] = next_node
				self.dfs(neighbor,next_node,visited)
			new_node.neighbors.append(visited[neighbor.label])

	def cloneGraph(self, node):
		"""
		:type node: UndirectedGraphNode
		:rtype: UndirectedGraphNode
		"""
		if node:
			visited = {}
			root = UndirectedGraphNode(node.label)
			visited[node.label] = root
			self.dfs(node,root,visited)
			return root
		else:
			return None