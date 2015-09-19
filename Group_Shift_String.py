class Solution(object):
	def normalize(self, s):
		result = ""
		if s == "":
			return result
		head = s[0]
		for word in s:
		    if ord(word) < ord(head):
		        result += chr(ord(word) + ord('z') + 1 - ord(head))
		    else:
			    result += chr(ord(word) - ord(head) + ord('a'))
		return result

	def groupStrings(self, strings):
		"""
		:type strings: List[str]
		:rtype: List[List[str]]
		"""
		s_hash = {}
		for s in strings:
			temp = self.normalize(s)
			if temp in s_hash:
				s_hash[temp].append(s)
			else:
				s_hash[temp] = [s]

		result = []
		for key in s_hash:
			new_list = s_hash[key]
			new_list.sort()
			result.append(new_list)
		return result
