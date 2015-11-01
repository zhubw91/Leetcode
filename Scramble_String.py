class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
        	return False
        l = len(s1)
        if l == 0:
        	return True
        f = [[[False for i in range(l)] for i in range(l)] for i in range(l)]
        for i in range(l):
        	for j in range(l):
        		if s1[i] == s2[j]:
        			f[0][i][j] = True

        for k in range(1,l):
        	for i in range(l-k-1,-1,-1):
        		for j in range(l-k-1,-1,-1):
        			for m in range(1,k+1):
        				if (f[m-1][i][j] and f[k-m][i+m][j+m]) or (f[m-1][i][j+k-m+1] and f[k-m][i+m][j]):
        					f[k][i][j] = True
        					break

        return f[l-1][0][0]
