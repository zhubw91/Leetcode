class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        last = A[0]
        dup = 0
        cnt = 0
        for i in range(1,len(A)):
            if A[i] == last and cnt > 0:
                dup = dup + 1
                cnt = cnt + 1
            elif A[i] == last:
                cnt = cnt + 1
            else:
                cnt = 0
            last = A[i]
            A[i-dup] = last
        return len(A) - dup 