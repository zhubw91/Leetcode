class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        if m == 0:
        	return 
        n = len(rooms[0])
        # find a gate and start BFS
        for i in range(m):
        	for j in range(n):
        		if rooms[i][j] == 0:
        			# BFS
        			q = [(i,j,rooms[i][j])]
        			visited = {(i,j):1}
        			head = 0
        			tail = 1
        			while head < tail:
        				x,y = q[head][0],q[head][1]
        				if x-1 >= 0 and (x-1,y) not in visited and rooms[x-1][y] > 0 and rooms[x][y] + 1 < rooms[x-1][y]:
        					q.append((x-1,y,rooms[x][y] + 1))
        					rooms[x-1][y] = rooms[x][y] + 1
        					tail += 1
        					visited[(x-1,y)] = 1
        				if x+1 < m and (x+1,y) not in visited and rooms[x+1][y] > 0 and rooms[x][y] + 1 < rooms[x+1][y]:
        					q.append((x+1,y,rooms[x][y] + 1))
        					rooms[x+1][y] = rooms[x][y] + 1
        					tail += 1
        					visited[(x+1,y)] = 1
        				if y-1 >= 0 and (x,y-1) not in visited and rooms[x][y-1] > 0 and rooms[x][y] + 1 < rooms[x][y-1]:
        					q.append((x,y-1,rooms[x][y] + 1))
        					rooms[x][y-1] = rooms[x][y] + 1
        					tail += 1
        					visited[(x,y-1)] = 1
        				if y+1 < n and (x,y+1) not in visited and rooms[x][y+1] > 0 and rooms[x][y] + 1 < rooms[x][y+1]:
        					q.append((x,y+1,rooms[x][y] + 1))
        					rooms[x][y-1] = rooms[x][y] + 1
        					tail += 1
        					visited[(x,y+1)] = 1
        				head += 1



