class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1 = []
        index2 = []
        for index,word in enumerate(words):
        	if word == word1:
        		index1.append(index)
        	elif word == word2:
        		index2.append(index)
        result = len(words)
        for i in index1:
        	for j in index2:
        		result = min(result, abs(i-j))
        return result
