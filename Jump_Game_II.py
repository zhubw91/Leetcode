class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if len(A) == 0:
        	return None
        if len(A) == 1:
        	return 0
        maxpace = 0
        minstep = 1
        top = 0
        tail = A[0]
        while tail < len(A)-1:
        	for i in range(top,tail+1):
        		maxpace = max(maxpace, i+A[i])
        	top = tail+1
        	tail= maxpace
        	minstep += 1
        return minstep
