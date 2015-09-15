class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 31
        result = 0
        while l >= 0:
        	r = n % 2
        	if r == 1:
        		result += 2 ** l
        	l -= 1
        	n /= 2
        return result
