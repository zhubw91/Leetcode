class Solution(object):
	def make_key(self, s):
		keyhash = [0]*26
		result = ""
		for word in s:
			keyhash[ord(word)-ord('a')] += 1
		for i in range(26):
			if keyhash[i] > 0:
				result += str(keyhash[i])+str(ord('a')+i)
		return result

	def groupAnagrams(self, strs):
		"""
		:type strs: List[str]
		:rtype: List[List[str]]
		"""
		anagram_hash = {}
		for s in strs:
			key = self.make_key(s)
			if key in anagram_hash:
				anagram_hash[key].append(s)
			else:
				anagram_hash[key] = [s]
		result = []
		for key in anagram_hash:
			new_list = anagram_hash[key]
			new_list.sort()
			result.append(new_list)
		return result
