class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        n = len(s)
        p1 = 0
        p2 = 1
        while p2 <= n:
        	if p2 == n or s[p2] == ' ':
        		for i in range((p2-p1)/2):
        			s[p1+i],s[p2-i-1] = s[p2-i-1],s[p1+i]
        		p1 = p2+1
        	p2 += 1
        p1 = 0
        p2 = n-1
        while p1 < p2:
        	s[p1],s[p2] = s[p2],s[p1]
        	p1 += 1
        	p2 -= 1 