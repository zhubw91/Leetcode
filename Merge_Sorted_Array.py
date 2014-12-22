class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i = 0
        j = 0
        k = 0
        while j < n:
        	if i >= m:
        		A[k] = B[j]
        		k = k + 1
        		j = j + 1
        	else:
        		if A[k] <= B[j]:
        			i = i + 1
        			k = k + 1
        		else:
        			A.insert(k,B[j])
        			j = j + 1
        			k = k + 1 