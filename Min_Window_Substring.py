class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        word_hash = {}
        cnt = 0
        for word in t:
        	if word not in word_hash:
        		word_hash[word] = 0
        		cnt += 1
        	word_hash[word] += 1
        head = 0
        tail = 0
        minlength = len(s) + 1
        x,y = 0,0
        while tail < len(s):
        	if s[tail] in word_hash:
        		word_hash[s[tail]] -= 1
        		if word_hash[s[tail]] == 0:
        			cnt -= 1
        	if cnt == 0:
        		while head < tail:
        			if s[head] in word_hash and word_hash[s[head]] == 0:
        				break
        			else:
        				if s[head] in word_hash:
        					word_hash[s[head]] += 1
        				head += 1
        				
        		if tail-head+1 < minlength:
        			minlength = tail-head+1
        			x,y = head,tail
        		
        		if s[head] in word_hash:
        			word_hash[s[head]] += 1
        		cnt += 1
        		head += 1
        		if head >= len(s):
        			break

        	tail += 1
        if minlength == len(s)+1:
        	return ""
        else:
        	return s[x:y+1]

solution = Solution()
solution.minWindow("a","b")


