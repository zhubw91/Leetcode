class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0 for i in range(n)] for i in range(n)]
        i,j,i_t,j_t = 0,0,0,1
        for k in range(n*n):
        	result[i][j] = k+1
        	if result[(i+i_t)%n][(j+j_t)%n]:
        		i_t,j_t = j_t,-i_t
        	i += i_t
        	j += j_t
        return result

