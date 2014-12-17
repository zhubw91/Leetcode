class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
        	return 0
        last = A[0]
        dup = 0
        for i in range(1,len(A)):
        	if A[i] == last:
        		dup = dup + 1
        	last = A[i]
        	A[i-dup] = last
        return len(A) - dup 