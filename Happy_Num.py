class Solution(object):
	def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		num_list = {}
		while n != 1:
			num_sum = 0
			while n>0:
				num_sum += (n%10)**2
				n /= 10
			if num_sum in num_list:
				return False
			n = num_sum
			num_list[n] = 1
		return True 
