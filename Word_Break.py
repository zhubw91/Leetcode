class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        wordhash = {}
        sephash = {}
        for word in dict:
        	wordhash[word] = 1
        def isSep(s,wordhash):
        	if sephash.has_key(s) is True:
        		return False
        	if wordhash.has_key(s) is True:
        		return True
        	for i in range(1,len(s)):
        		if wordhash.has_key(s[:i]) == 1 and isSep(s[i:],wordhash) is True:
        			return True
        	if sephash.has_key(s) is False:
        		sephash[s] = 1
        	return False
        return isSep(s,wordhash)
