class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbr = {}
        self.dic = {}
        for word in dictionary:
            l = len(word)
            self.dic[word] = 1
            if l<=2:
                s = word
            else:
                s = word[0] + str(l-2) + word[-1]
            if s not in self.abbr:
                self.abbr[s] = 1
            else:
                self.abbr[s] += 1
        

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        l = len(word)
        if l<=2:
            s = word
        else:
            s = word[0] + str(l-2) + word[-1]
        if s in self.abbr:
            if word in self.dic and self.abbr[s] == 1:
                return True
            else:
                return False
        else:
            return True

        


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")