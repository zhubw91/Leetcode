class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        fre = {}
        odd = 0
        for word in s:
        	if word in fre:
        		fre[word] += 1
        		if fre[word]%2 == 0:
        			odd -= 1
        		else:
        			odd += 1
        	else:
        		fre[word] = 1
        		odd += 1
        if odd > 1:
        	return False
        else:
        	return True
