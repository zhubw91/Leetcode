class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) == 0:
        	return None
        premin = A[0]
        premax = A[0]
        result = A[0]
        for index,num in enumerate(A):
        	if index == 0:
        		continue
        	tempmax = max(premax*num, num, premin*num)
        	tempmin = min(premin*num, num, premax*num)
        	premax = tempmax
        	premin = tempmin
        	result = max(tempmax, result)
        return result
