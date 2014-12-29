class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
    	if numRows == 0:
    		return []
        result = [[1]]
        for i in range(1,numRows):
        	last = result[i-1]
        	now = [0] * (i+1)
        	now[0] = 1
        	for j in range(1,i):
        		now[j] = last[j] + last[j-1]
        	now[i] = 1
        	result.append(now)
        return result
