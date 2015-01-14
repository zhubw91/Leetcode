class Solution:
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        f = [[0 for col in range(n+1)] for row in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if obstacleGrid[i-1][j-1] == 1:
                    continue
                if i is 1 or j is 1:
                    if i is 1 and j is 1:
                        f[i][j] = 1
                    if i is 1 and f[i][j-1] != 0:
                        f[i][j] = 1
                    if j is 1 and f[i-1][j] != 0:
                        f[i][j] = 1
                else:
                    f[i][j] = f[i-1][j] + f[i][j-1]
        return f[m][n]