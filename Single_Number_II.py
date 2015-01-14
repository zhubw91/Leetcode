class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones = twos = threes = 0
        for num in A:
        	twos |= ones & num
        	ones ^= num
        	threes = ones & twos
        	ones &= ~threes
        	twos &= ~threes
        return ones