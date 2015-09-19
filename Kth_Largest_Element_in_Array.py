class Solution(object):
	def quick_select(self, nums, k, start, end):
		pivot = nums[start]
		i = start
		j = end
		while i<j:
			while i<j and nums[j] <= pivot:
				j -= 1
			nums[i] = nums[j]
			while i<j and nums[i] >= pivot:
				i += 1
			nums[j] = nums[i]
		nums[i] = pivot
		if i - start == k-1:
			return nums[i]
		elif i - start < k-1:
			return self.quick_select(nums, k-(i-start+1), i+1, end)
		else:
			return self.quick_select(nums, k, start, i-1) 

	def findKthLargest(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		return self.quick_select(nums, k, 0, len(nums)-1)