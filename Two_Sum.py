class Solution:
    # @return a tuple, (index1, index2)
	def twoSum(self, num, target):
		h = {}
		i = 1
		for item in num:
			if h.has_key(target-item):
				if h[target-item] < i:
					return h[target-item],i
				else:
					return (i,h[target-item])
			h[item] = i
			i = i + 1