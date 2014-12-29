class Solution:
	# @return a string	
	def convert(self, s, nRows):
		result = ""
		if nRows == 1:
				return s
		j = 0
		while j < len(s):
			result = result + s[j]
			j = j + 2*(nRows - 1)
		for i in range(1,nRows-1):
			j = i
			while j < len(s):
				result = result + s[j]
				j = j + 2*(nRows - 1 - i)
				if j < len(s):
					result = result + s[j]
				j = j + 2*i
		j = nRows - 1
		while j < len(s):
			result = result + s[j]
			j = j + 2*(nRows - 1)
		return result

