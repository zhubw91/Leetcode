class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        result = 0
        maximum = A[0]
        for item in A:
        	result = result + item
        	if result > maximum:
        		maximum = result
        	if result < 0:
        		result = 0
        return maximum

