class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l_s = len(s)
        l_t = len(t)
        if abs(l_t - l_s) > 1:
        	return False
        i, j = 0, 0
        error = 0
        while i < l_s and j < l_t:
        	if s[i] == t[j]:
        		i += 1
        		j += 1
        	elif i+1 < l_s and s[i+1] == t[j]:
        		error += 1
        		i += 1
        	elif j+1 < l_t and s[i] == t[j+1]:
        		error += 1
        		j += 1
        	elif i+1 < l_s and j+1<l_t and s[i+1] == t[j+1]:
        		error += 1
        		i += 1
        		j += 1
        	else:
        		i += 1
        		j += 1
        		error += 1
        	if error > 1:
        		return False
        if i < l_s or j < l_t:
        	error += 1
        if error != 1:
        	return False
        else:
        	return True


