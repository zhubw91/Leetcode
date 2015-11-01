class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        n = len(wordList)
        if n == 0:
        	return 0
        m = len(beginWord)
        q = [(beginWord,1)]
        bfs_hash = {beginWord:1}
        head = 0
        tail = 1
        while head < tail:
        	current,cnt = q[head]
        	if current not in wordList:
        		break
        	for i in range(m):
        		x = current[i]
        		for j in range(26):
        			y = chr(ord('a')+j)
        			if x == y:
        				continue
        			temp = ""
        			temp = current[:i] + y + current[i+1:]
        			if temp in wordList and temp not in bfs_hash:
        				if temp == endWord:
        					return cnt + 1
        				q.append((temp,cnt+1))
        				tail += 1
        	head += 1
        return 0