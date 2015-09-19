class Solution(object):
	def firstMissingPositive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		for i in range(n):
			if i+1 == nums[i]:
				continue
			x = nums[i]
			while x > 0  and x <= n and x != nums[x-1]:
				nums[i], nums[x-1] = nums[x-1], nums[i]
				x = nums[i]

		for i in range(n):
			if i+1 != nums[i]:
				return i+1
		return n+1