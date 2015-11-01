class Solution(object):
	def wordPattern(self, pattern, str):
		"""
		:type pattern: str
		:type str: str
		:rtype: bool
		"""
		if pattern == None or len(pattern) == 0 or str == None:
			return False
		s = str.split()
		if len(pattern) != len(s):
			return False
		word_map = {}
		word_hash = {}
		for i in range(len(pattern)):
			word1 = pattern[i]
			word2 = s[i]
			if word1 in word_map:
				if word_map[word1] != word2:
					return False
			else:
				if word2 in word_hash:
					return False
				word_map[word1] = word2
				word_hash[word2] = 1

		return True

