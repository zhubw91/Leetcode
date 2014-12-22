class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        low = 0
        high = len(A) - 1
        while low < high:
        	mid = (low + high)/2
        	if A[mid] is target:
        		return mid
        	elif A[mid] < target:
        		low = mid + 1
        	else:
        		high = mid - 1
        if A[low] >= target:
        	return low
        else:
        	return low + 1