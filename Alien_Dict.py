class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        g = {}
        d = {}
        for word in words:
        	for letter in word:
        		d[letter] = 0
        		g[letter] = {}

        l = len(words)
        for i in range(l-1):
        	ll = min(len(words[i]),len(words[i+1]))
        	for j in range(ll):
        		if words[i][j] == words[i+1][j]:
        			continue
        		g[words[i][j]][words[i+1][j]] = 1
        		d[words[i+1][j]] += 1
        		break

        	
        q = []
        visited = {}
        for letter in d:
        	if d[letter] == 0:
        		q.append(letter)
        		visited[letter] = 1
        		break
        if len(q) == 0:
        	return ""
        head = 0
        tail = 1
        while head < tail:
        	node = q[head]
        	for x in g[node]:
        		d[x] -= 1
        	for x in d:
        		if x in visited:
        			continue
        		if d[x] == 0:
        			q.append(x)
        			visited[x] = 1
        			tail += 1
        	head += 1
        if len(q) != len(d):
        	return ""
        result = ""
        for x in q:
        	result += x
        return result