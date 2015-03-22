class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
        	return 0
        letter = {}
        n = len(s)
        i = 0
        j = 1
        l = 1
        result = 1
        letter[s[0]] = 0
        while j < n:
        	if letter.has_key(s[j]) is True:
        		while s[i] != s[j]:
        			del letter[s[i]]
        			l -= 1
        			i += 1
        		del letter[s[i]]
        		i += 1
        		l -= 1

        	else:
        		letter[s[j]] = 0
        		j += 1
        		l += 1
        		result = max(result,l)
        return result
