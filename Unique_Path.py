class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        f = [[0 for col in range(n+1)] for row in range(m+1)]
        for i in range(1,m+1):
        	for j in range(1,n+1):
        		if i is 1 or j is 1:
        			f[i][j] = 1
        		else:
        			f[i][j] = f[i-1][j] + f[i][j-1]
        return f[m][n]