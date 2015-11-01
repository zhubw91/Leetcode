class Solution(object):
	def hIndex(self, citations):
		"""
		:type citations: List[int]
		:rtype: int
		"""
		left = 0
		l = len(citations)
		right = l-1
		result = 0
		while left <= right:
			mid = (left+right)/2
			if citations[mid]>=l-mid:
				result = l-mid
				right = mid-1
			else:
				left = mid+1
		return result

