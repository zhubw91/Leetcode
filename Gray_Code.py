class Solution:
    # @return a list of integers
    def grayCode(self, n):
        num = [0,1]
        if n == 0:
            return [0]
        if n == 1:
        	return num
        for i in range(1,n):
        	new = [0]*(2*len(num))
        	for j in range(len(num)):
        		new[j] = num[j]
        		new[len(new)-j-1] = num[j] + 2**i
        	num = new
        return num