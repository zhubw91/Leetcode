class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        word_hash = {}
        for word in s:
        	if word_hash.has_key(word) == False:
        		word_hash[word] = 1
        	else:
        		word_hash[word] += 1
        for word in t:
        	if word_hash.has_key(word) == False:
        		return False
        	else:
        		word_hash[word] -= 1
        		if word_hash[word] < 0:
        			return False
        for key in word_hash:
        	if word_hash[key] > 0:
        		return False
        return True
