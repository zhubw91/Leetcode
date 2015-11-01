class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        word_hash = {}
        not_split_hash = {}
        for w in wordDict:
        	word_hash[w] = 1
        result = []
        def dfs(s,stack):
        	flag = 0
        	if s in not_split_hash:
        		return 0
        	if s in word_hash:
        		stack.append(s)
        		result.append(" ".join(stack))
        		for i in range(1,len(stack)):
        			split_hash["".join(stack[i:])] = stack[i:]

        		flag = 1
        		stack.pop()
        	for i in range(1,len(s)):
        		if s[:i] in word_hash:
        			stack.append(s[:i])
        			if dfs(s[i:],stack) == 1:
        				flag = 1
        			stack.pop()
        	if flag == 0:
        		not_split_hash[s] = 1
        	return flag
        stack = []
        dfs(s,stack)
        return result