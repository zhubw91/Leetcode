class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
	def pow(self, x, n):
		t = 2
		f = [1,x]
		result = 1
		op = 1
		if n < 0:
			op = -1
			n = -n
		while t <= n:
			f.append(f[-1]*f[-1])
			t = t << 1
		t = t >> 1
		while n > 0:
			if t <= n:
				result *= f[-1]
				n -= t
			f.pop()
			t = t >> 1
		return result if op == 1 else 1.0/result

