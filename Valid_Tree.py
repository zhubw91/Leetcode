class Solution(object):
	def dfs(self,start_node, g, visited, edge_visited):
		if start_node not in g:
			return True
		for des_node in g[start_node]:
			if (start_node,des_node) in edge_visited:
				continue
			if des_node in visited:
				return False
			visited[des_node] = 1
			edge_visited[(start_node,des_node)] = 1
			edge_visited[(des_node,start_node)] = 1
			if self.dfs(des_node, g, visited, edge_visited) == False:
				return False
		return True

	def validTree(self,n, edges):
		"""
		:type n: int
		:type edges: List[List[int]]
		:rtype: bool
		"""
		# construct adjacent list for graph
		g = {}
		for edge in edges:
			if edge[0] not in g:
				g[edge[0]] = []
			if edge[1] not in g:
				g[edge[1]] = []
			g[edge[0]].append(edge[1])
			g[edge[1]].append(edge[0])
		# dfs
		visited = {}
		edge_visited = {}
		visited[0] = 1

		if self.dfs(0,g,visited,edge_visited) == False or len(visited) != n:
			return False
		else:
			return True