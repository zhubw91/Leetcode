class Solution(object):
	def dis(self, a, b, t):
		if (a > 0 and b > 0) or (a < 0 and b < 0):
			if abs(a-b) <= t:
				return True
			else:
				return False
		else:
			if max(a,b) > t:
				return False
			elif t - max(a,b) < -min(a,b):
				return False
			else:
				return True

	def containsNearbyAlmostDuplicate(self, nums, k, t):
		"""
		:type nums: List[int]
		:type k: int
		:type t: int
		:rtype: bool
		"""
		num_hash = {}

		for index,x in enumerate(nums):
			if len(nums) > 2*t:
				for i in range(x-t,x+t+1):
					if i in num_hash and abs(index - num_hash[i]) <= k:
						return True
			else: 
				for y in num_hash:
					if self.dis(x,y,t) and abs(num_hash[y] - index) <= k:
						return True
			num_hash[x] = index
		return False