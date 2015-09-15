class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n == 0:
        	return True
        else if n == 1:
        	return False
        else if n%2 == 1:
        	return False
        else:
        	return n>>1
