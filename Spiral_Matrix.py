class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        result = []
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        m = len(matrix)
        if m == 0:
        	return result
        n = len(matrix[0])
        k = 0
        i = 0
        j = -1
        d = 0
        rest = n
        dim1 = n
        dim2 = m
        while k < m*n:
        	for t in range(rest):
        		
        		i += direction[d][0]
        		j += direction[d][1]
        		result.append(matrix[i][j])
        		k += 1
        	dim1,dim2 = dim2,dim1
        	dim1 -= 1
        	rest = dim1
        	d = (d+1)%4
        return result
