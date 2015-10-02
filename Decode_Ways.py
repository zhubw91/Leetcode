class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        f = [0]*(n+1)
        if n == 0:
        	return 0
        if n == 1:
        	if s == "0":
        		return 0
        	else:
        		return 1
        if s[0] == '0':
        	return 0
        f[0] = 1
        f[1] = 1
        for i in range(1,n):
        	if int(s[i-1]+s[i]) <= 26 and int(s[i-1]+s[i]) >=1:
        		if s[i] == '0':
        			f[i+1] = f[i-1]
        		elif s[i-1] == '0':
        			f[i+1] = f[i]
        		else:
        			f[i+1] = f[i-1] + f[i]
        	elif int(s[i-1]+s[i]) == 0:
        		return 0
        	elif s[i] == '0':
        		return 0
        	else:
        		f[i+1] = f[i]
        return f[n] 