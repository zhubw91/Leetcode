class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        t = 1
        b = 0
        while n > 0:
        	a = n%10
        	n /= 10
        	result += n*t
        	if a == 1:
        		result += 1 + b
        	elif a >= 2:
        		result += t
        	b = a*t + b
        	t *= 10
        return result
