class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.word_hash = {}
        for i,word in enumerate(words):
            if word in self.word_hash:
                self.word_hash[word].append(i)
            else:
                self.word_hash[word] = [i]
        

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        a = self.word_hash[word1]
        b = self.word_hash[word2]
        result = abs(a[0] - b[0])
        for i in a:
            for j in b:
                result = min(result, abs(i-j))
        return result

        


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")