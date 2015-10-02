class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i = -len(words)
        j = -len(words)
        result = len(words)
        for index,word in enumerate(words):
        	if word1 == word:
        		if word1 == word2:
        			result = min(result, index-i)
        			i = index
        		else:
        			i = index
        			result = min(result, i-j)
        	if word2 == word and word1 != word2:
        		j = index
        		result = min(result, j-i)
        return result