class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words = s.split()
        result = ''
        n = len(words)
        for i in range(n):
        	result += words[n-i-1]
        	if i < n-1:
        		result += ' '
        return result
