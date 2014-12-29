class Solution:
    # @return a string
    def convertToTitle(self, num):
        result = ''
        a = []
        while num > 0:
        	b = num%26
        	a.append(b)
        	num = num / 26
        	if b == 0:
        		a[-1] = 26
        		num -= 1
        for i in range(len(a)):
        	result += chr(a[len(a) - i - 1] - 1 + ord('A'))
        return result