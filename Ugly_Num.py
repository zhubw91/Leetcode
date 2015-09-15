class Solution:
    # @param {integer} num
    # @return {boolean}
    def isUgly(self, num):
        while(num>1 and num%2 == 0):
        	num /= 2
        while(num>1 and num%3 == 0):
        	num /= 3
        while(num>1 and num%5 == 0):
        	num /= 5
        if num == 1:
        	return True
        else:
        	return False