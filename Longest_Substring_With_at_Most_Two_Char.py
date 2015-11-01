class Solution(object):
	def lengthOfLongestSubstringTwoDistinct(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		char_hash = {}
		if len(s) == 0:
			return 0
		cnt = 1
		result = 1
		p1 = 0
		p2 = 1
		char_hash[s[0]] = 1
		while p2 < len(s):
			if s[p2] not in char_hash or char_hash[s[p2]] == 0:
				cnt += 1
				char_hash[s[p2]] = 1
			else:
				char_hash[s[p2]] += 1
			while cnt > 2:
				char_hash[s[p1]] -= 1
				if char_hash[s[p1]] == 0:
					cnt -= 1
				p1 += 1
			result = max(result,p2-p1+1)
			p2 += 1
		return result
