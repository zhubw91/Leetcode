class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        t = target - 0.5
        start = 0
        end = len(A) - 1
        while start <= end:
        	mid = (start + end)/2
        	if A[mid] > t:
        		end = mid - 1
        	else:
        		start = mid + 1
        if start >= len(A) or A[start] != target:
        	return [-1,-1]
        a = start
        t = target + 0.5
        start = 0
        end = len(A) - 1
        while start <= end:
        	mid = (start + end)/2
        	if A[mid] > t:
        		end = mid - 1
        	else:
        		start = mid + 1
        b = end
        return [a,b]


