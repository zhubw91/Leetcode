class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        word_hash = {}
        n = len(words)
        if n == 0:
        	return result
        m = len(words[0])
        cnt = 0
        for word in words:
        	if word in word_hash:
        		word_hash[word] += 1
        	else:
        		word_hash[word] = 1
        for i in range(m):
        	temp_hash = {}
        	head = i
        	tail = i
        	cnt = 0
        	while tail <= len(s)-m:
        		temp = s[tail:tail+m]
        		if temp not in word_hash:
        			head = tail+m
        			tail += m
        			temp_hash = {}
        			cnt = 0
        			continue
        		if temp in temp_hash:
        			temp_hash[temp] += 1
        		else:
        			temp_hash[temp] = 1
        		cnt += 1
        		while cnt > n or temp_hash[temp] > word_hash[temp]:
        			head_temp = s[head:head+m]
        			temp_hash[head_temp] -= 1
        			cnt -= 1
        			head += m
        		
        		if cnt == n:
        			result.append(head)
        		tail += m

        return result