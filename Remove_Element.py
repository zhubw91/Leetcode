class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        r = 0
        for i in range(len(A)):
        	if A[i] is elem:
        		r = r + 1
        	else:
        		A[i-r] = A[i]
        return len(A) - r
