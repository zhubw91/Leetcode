class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        result = 1
        while result*result < x:
        	result = result << 1
        if result*result == x:
        	return result
        result = result >> 1
        t = result >> 1
        while t > 0:
        	while result*result <= x:
        		result += t
        	result -= t
        	t = t >> 1
        return result