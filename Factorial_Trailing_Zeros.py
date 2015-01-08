class Solution:
    # @return an integer
    def trailingZeroes(self, n):
    	t = 5
    	result = 0
    	while t <= n:
    		result += n/t
    		t *= 5
        return result