class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        start = -1
        maxl = 0
        for i in range(len(s)):
        	if s[i] == '(':
        		stack.append(i)
        	else:
        		if len(stack) == 0:
        			start = i
        		else:
        			stack.pop()
        			if len(stack) == 0:
        				maxl = max(maxl, i-start)
        			else:
        				maxl = max(maxl, i-stack[-1])
        return maxl
