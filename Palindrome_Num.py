class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
        	return False
        div_high = 1
        div_low = 1
        while x/div_high >= 10:
        	div_high *= 10
        while div_high > div_low:
        	if (x/div_high)%10 != (x/div_low)%10:
        		return False
        	div_high /= 10
        	div_low *= 10
        return True