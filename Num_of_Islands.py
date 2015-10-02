class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == None:
        	return 0
        m = len(grid)
        if m == 0:
        	return 0
        n = len(grid[0])
        num = 1
        for i in range(m):
        	for j in range(n):
        		if grid[i][j] != '1':
        			continue
        		stack = [(i,j)]
        		num += 1
        		top = 0
        		while top >=0:
        			x,y = stack[top]
        			grid[x][y] = str(num)
        			if x+1 < m and grid[x+1][y] == '1':
        				stack.append((x+1,y))
        				top += 1
        			elif x-1 >= 0 and grid[x-1][y] == '1':
        				stack.append((x-1,y))
        				top += 1
        			elif y+1 < n and grid[x][y+1] == '1':
        				stack.append((x,y+1))
        				top += 1
        			elif y-1 >= 0 and grid[x][y-1] == '1':
        				stack.append((x,y-1))
        				top += 1
        			else:
        				stack.pop()
        				top -= 1
        return num-1