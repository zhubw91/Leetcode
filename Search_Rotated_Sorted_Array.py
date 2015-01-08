class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        start = 0
        end = len(A) - 1
        while start <= end:
        	mid = (start + end)/2
        	if A[mid] == target:
        		return mid
        	if A[start] <= A[mid] and A[mid] <= A[end]:
        		if A[mid] < target:
        			start = mid + 1
        		else:
        			end = mid - 1
        	elif A[start] <= A[mid]:
        		if target < A[mid] and target >= A[start]:
        			end = mid - 1
        		else:
        			start = mid + 1
        	else:
        		if target > A[mid] and target <= A[end]:
        			start = mid + 1
        		else:
        			end = mid - 1
        return -1