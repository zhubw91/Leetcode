class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0 or k == 0:
        	return 0
        f = [0] * 2
        f[0] = 0
        f[1] = k
        for i in range(1,n):
        	s = f[0]
        	f[0] = f[1]
        	f[1] = (f[1] + s) * (k-1)
        	
        return f[0] + f[1]

