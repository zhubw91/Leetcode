class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        start = 0
        end = len(A) - 1
        def subsearch(A, target, start, end):
            if start > end:
                return False
            mid = (start + end)/2
            if A[mid] == target:
                return True
            if A[start] < A[mid] and A[mid] < A[end]:
                if A[mid] < target:
                    return subsearch(A, target, mid+1, end)
                else:
                    return subsearch(A, target, start, mid-1)
            elif A[start] < A[mid] and target > A[mid]:
                return subsearch(A, target, mid+1, end)
            elif A[mid] < A[end] and target < A[mid]:
                return subsearch(A, target, start, mid-1)
            else:
                return subsearch(A, target, start, mid-1) or subsearch(A, target, mid+1, end)
            return False
        return subsearch(A, target, start, end)