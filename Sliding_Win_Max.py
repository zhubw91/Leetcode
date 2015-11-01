import collections
class Solution(object):
	def maxSlidingWindow(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		q = collections.deque()
		result = []
		for i in range(len(nums)):
			while len(q) > 0 and q[0] < i-k+1:
				q.popleft()
			while len(q) > 0 and nums[q[-1]] < nums[i]:
				q.pop()
			q.append(i)
			if i >= k-1:
				result.append(nums[q[0]])
		return result