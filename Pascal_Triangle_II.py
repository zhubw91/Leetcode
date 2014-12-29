class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        result = []
        for i in range(0,rowIndex+1):
        	result.append(1)
        	for j in range(1,i):
        		k = len(result) - j - 1
        		result[k] = result[k] + result[k-1]
        return result
