class Solution(object):
	def __init__(self):
		self.state = {}
	def canWin(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		l = len(s)
		if s in self.state:
			return self.state[s]
		for i in range(l-1):
			if s[i:i+2] != "++":
				continue
			new_s = s[:i] + "--" + s[i+2:]
			if self.canWin(new_s) == False:
				self.state[s] = True
				return True
		self.state[s] = False
		return False