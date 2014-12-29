class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if s == "":
        	return True
        i = 0
        j = len(s) - 1
        while i < j:
        	while  i < len(s) and str.isalpha(s[i]) is False and str.isdigit(s[i]) is False:
        		i = i + 1
        	while j >= 0 and str.isalpha(s[j]) is False and str.isdigit(s[j]) is False:
        		j = j - 1
        	if i >= len(s) or j < 0:
        		break
        	if s[i].upper() != s[j].upper():
        		return False
        	i = i + 1
        	j = j - 1
        	
        return True