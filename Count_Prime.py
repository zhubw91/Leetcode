class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        prime_hash = {}
        prime_num = max(0, n-2)
        for i in range(2, n):
        	if prime_hash.has_key(i):
        		continue
        	if i * i >= n:
        		break
        	j = i * i
        	while j < n:
        		prime_hash[j] = 1
        		prime_num -= 1
        		j += i
        return prime_num