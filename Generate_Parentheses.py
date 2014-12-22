class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        par = ['(',')']
        result = []
        s = [1]
        r = 0
        temp = -1
        while len(s) > 0:
        	if len(s) is 2*n+1:
        		if r is 0:
        			p = ''
        			for i in range(1,len(s)):
        				p = p + par[s[i]]
        			result.append(p)
        		temp = s.pop()
        		if temp is 0:
        			r = r - 1
        		else:
        			r = r + 1
        	elif temp is 1 or r < 0:
        		temp = s.pop()
        		if temp is 0:
        			r = r - 1
        		else:
        			r = r + 1
        	else:
        		s.append(temp+1)
        		if temp is -1:
        			r = r + 1
        		else:
        			r = r - 1
        		temp = -1
        return result
