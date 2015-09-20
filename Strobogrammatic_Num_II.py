class Solution(object):
	def make(self, n):
		num_hash = {'1':'1','0':'0','8':'8','6':'9','9':'6'}
		if n == 1:
			return ["1","8","0"]
		elif n == 0:
			return [""]
		else:
			result = []
			temp = self.make(n-2)
			for s in temp:
				for key in num_hash:
					result.append(key+s+num_hash[key])
			return result

	def findStrobogrammatic(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		if n<=1:
			result = self.make(n)
		else:
			temp = self.make(n-2)
			num_hash = {'1':'1','8':'8','6':'9','9':'6'}
			result = []
			for s in temp:
				for key in num_hash:
					result.append(key+s+num_hash[key])
		return result


