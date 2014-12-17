class Solution:
    # @return a string
    def countAndSay(self, n):
		s = '1'
		if n == 1:
			return s
		for i in range(1,n):
			t = ''
			last = s[0]
			cnt = 0
			for word in s:
				if word == last:
					cnt = cnt + 1
				else:
					t = t + str(cnt) + last
					last = word
					cnt = 1
			t = t + str(cnt) + last
			s = t
		return s