class Solution:
    # @param n, an integer
    # @return an integer

    def climbStairs(self, n):
        lastlast = 0
        last = 1
        for i in range(1,n+1):
        	result = last + lastlast
        	lastlast = last
        	last = result 
        return result
