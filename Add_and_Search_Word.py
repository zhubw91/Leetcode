class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.is_word = True

        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        q = [(self.root,0)]
        head = 0
        tail = 1
        while head < tail:
            node,i = q[head]
            if i == len(word):
                if node.is_word == True:
                    return True
                else:
                    head += 1
                    continue
            if word[i] == '.':
                for key in node.children:
                    q.append((node.children[key],i+1))
                    tail += 1
            elif word[i] in node.children:
                q.append((node.children[word[i]],i+1))
                tail += 1
            head += 1
        return False


        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")