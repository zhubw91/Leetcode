class Solution(object):
	def canFinish(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: bool
		"""
		g = {}
		degree = [0]*numCourses
		for i in range(numCourses):
			g[i] = []
		for edge in prerequisites:
			g[edge[1]].append(edge[0])
			degree[edge[0]] += 1
		head = 0
		tail = 0
		hash_set = {}
		q = []
		for i in range(numCourses):
			if degree[i] == 0:
				q.append(i)
				tail = 1
				hash_set[i] = 1
				break
		while head < tail:
			for x in g[q[head]]:
				degree[x] -= 1
			for x in range(numCourses):
				if x in hash_set:
					continue
				if degree[x] == 0:
					q.append(x)
					tail += 1
					hash_set[x] = 1
			head += 1
		if len(hash_set) == numCourses:
			return True
		else:
			return False

