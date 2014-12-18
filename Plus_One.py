class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        r = 1
        for i in range(0,len(digits)):
        	j = len(digits) - i - 1
        	digits[j] = digits[j] + r
        	if digits[j] > 9:
        		digits[j] = digits[j] - 10
        		r = 1
        	else:
        		r = 0
        		break
        if r == 1:
        	digits.insert(0,1)
        return digits
