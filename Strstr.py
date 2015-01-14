class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        skip = {}
        n = len(haystack)
        m = len(needle)
        if m>n:
        	return -1
        for i,c in enumerate(needle):
        	skip[c] = m - i
        pos = 0
        while pos <= n - m:
        	flag = 0
        	for i in range(m):
        		if haystack[pos+i] != needle[i]:
        			if pos == n - m:
        				return -1
        			else:
        				if skip.has_key(haystack[pos+m]) == False:
        					pos += m + 1
        				else:
        					pos += skip[haystack[pos+m]]
        			flag = 1
        			break
        	if flag == 0:
        		return pos
        return -1



