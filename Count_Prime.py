class Solution:
	# @param {integer} n
	# @return {integer}
	def countPrimes(self, n):
		prime_hash = [False]*(n+1)
		prime_num = max(0, n-2)
		m = int(n**0.5)+1
		for i in range(2, m):
			if prime_hash[i]:
				continue
			j = i * i
			while j < n:
				if prime_hash[j] == False:
					prime_hash[j] = True
					prime_num -= 1
				j += i
		return prime_num