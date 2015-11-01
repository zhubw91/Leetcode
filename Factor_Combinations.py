class Solution(object):
	def f(self, result, current, min_fac, n):
		if n<=1:
			if len(current) > 1:
				result.append(current)
		else:
			for i in range(min_fac,n):
				if i*i > n:
					break
				if n%i == 0:
					current.append(i)
					self.f(result,current,i,n/i)
					current.pop() 
	def getFactors(self, n):
		"""
		:type n: int
		:rtype: List[List[int]]
		"""
		result = []
		current = []
		self.f(result,current,2,n)
		return result