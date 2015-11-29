class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        g = []
        for i in range(numCourses):
        	g.append([])
        d = [0]*numCourses
        for item in prerequisites:
        	g[item[1]].append(item[0])
        	d[item[0]] += 1
        q = []
        head = 0
        tail = 0
        is_visited = [0]*numCourses
        for i in range(numCourses):
        	if d[i] == 0:
        		q.append(i)
        		tail += 1
        		is_visited[i] = 1
        while head < tail:
        	x = q[head]
        	for node in g[x]:
        		d[node] -= 1
        	for i in range(numCourses):
        		if is_visited[i] == 1:
        			continue
        		if d[i] == 0:
        			q.append(i)
        			tail += 1
        			is_visited[i] = 1
        	head += 1
        if len(q) != numCourses:
        	return []
        else:
        	return q
solution = Solution()
print solution.findOrder(3,[[0,1],[0,2],[1,2]])

