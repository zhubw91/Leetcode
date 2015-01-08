class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        f = [[0 for col in range(n)]for row in range(m)]
        for i in range(m):
        	for j in range(n):
        		if i == 0 and j == 0:
        		    f[i][j] = grid[i][j]
        		elif i == 0:
        		    f[i][j] = f[i][j-1] + grid[i][j]
        		elif j == 0:
        			f[i][j] = f[i-1][j] + grid[i][j]
        		else:
        			f[i][j] = min(f[i-1][j],f[i][j-1]) + grid[i][j]
        return f[m-1][n-1]
