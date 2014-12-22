class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
    	row0 = 1
    	for item in matrix[0]:
    		if item is 0:
    			row0 = 0
    			break;
    	for i in range(1,len(matrix)):
    		for j in range(len(matrix[0])):
    			if matrix[i][j] is 0:
    				matrix[i][0] = 0
    				matrix[0][j] = 0
    	for i in range(1,len(matrix)):
    		for j in range(1,len(matrix[0])):
    			if matrix[i][0] is 0 or matrix[0][j] is 0:
    				matrix[i][j] = 0
    	for i in range(1,len(matrix)):
    		if matrix[0][0] is 0:
    			matrix[i][0] = 0
    	for j in range(len(matrix[0])):
    		if row0 is 0:
    			matrix[0][j] = 0
        