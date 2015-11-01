class Solution(object):
	def findMissingRanges(self, nums, lower, upper):
		"""
		:type nums: List[int]
		:type lower: int
		:type upper: int
		:rtype: List[str]
		"""
		x = lower
		result = []
		for num in nums:
			if num > upper:
				if x == upper:
					result.append(str(x))
					x = upper+1
				elif x < upper:
					result.append(str(x) + "->" + str(upper))
					x = upper+1
				break
			if num < lower:
				continue

			if num == x:
				x = num + 1
			elif num == x+1:
				result.append(str(x))
				x = num + 1
			else:
				result.append(str(x) + "->" + str(num-1)) 
				x = num + 1
		if x == upper:
			result.append(str(x))
		elif x < upper:
			result.append(str(x) + "->" + str(upper))
		return result

