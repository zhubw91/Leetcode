class Solution(object):
	def helper(self, k, result, stack, rest_sum):
		if len(stack) == k:
			# add new combination
			if rest_sum == 0:
				new_stack = stack[:]
				result.append(new_stack)
			return

		if len(stack) == 0:
			t = 1
		else:
			t = stack[-1] + 1
		for i in range(t,min(rest_sum+1,10)):
			stack.append(i)
			self.helper(k, result, stack, rest_sum - i)
			stack.pop()
		return
	def combinationSum3(self, k, n):
		"""
		:type k: int
		:type n: int
		:rtype: List[List[int]]
		"""
		result = []
		stack = []
		self.helper(k, result, stack, n)
		return result
