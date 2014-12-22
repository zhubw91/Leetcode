class Solution:
    # @return an integer
    def reverse(self, x):
        result = 0
        r = 1
        if x < 0:
    	    r = -1
    	    x = r*x
        while x > 0:
        	result = result*10 + x%10
        	x = x / 10
        	if x > 0 and result > 2147483647 / 10:
        		return 0
        return result*r
