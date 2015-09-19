class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m > 0:
        	n = len(matrix[0])
        else:
        	n = 0
        result = 0
        f = [[0 for x in range(n)] for x in range(m)]
        if n > 0:
        	for i in range(m):
        		f[i][0] = int(matrix[i][0])
        		result = max(result,f[i][0])
        if m > 0:
        	for i in range(n):
        		f[0][i] = int(matrix[0][i])
        		result = max(result,f[0][i])
        for i in range(1,m):
        	for j in range(1,n):
        		if matrix[i][j] == '0':
        			f[i][j] = 0
        		else:
        			f[i][j] = min(f[i-1][j-1],f[i-1][j],f[i][j-1]) + 1
        			result = max(f[i][j], result)
        return result**2


