class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        maxjump = 1
        for i in range(len(A)-1):
        	maxjump = max(maxjump-1,A[i])
        	if maxjump == 0:
        		return False
        if maxjump > 0:
        	return True
        else:
        	return False