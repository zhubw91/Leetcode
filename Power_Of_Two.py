class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        while n > 0:
            if n == 1:
                return True
            if n%2 != 0:
                return False
            else:
                n /= 2
        return False