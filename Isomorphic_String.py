class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_s = {}
        hash_t = {}
        n = len(s)
        for i in range(n):
        	if hash_s.has_key(s[i]) and hash_t.has_key(t[i]):
        		if hash_s[s[i]] != hash_t[t[i]]:
        			return False
        	elif hash_s.has_key(s[i]) == False and hash_t.has_key(t[i]) == False:
        		hash_s[s[i]] = i
        		hash_t[t[i]] = i
        	else:
        		return False
        return True