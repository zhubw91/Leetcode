class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
    	n = len(num)
    	isused = [0]*n
    	result = []
    	def recursive(temp,index):
    		if index == n:
    			haha = temp[:]
    			result.append(haha)
    		else:
    			for i in range(n):
    				if isused[i] == 0:
    					temp.append(num[i])
    					isused[i] = 1
    					recursive(temp,index+1)
    					isused[i] = 0
    					temp.pop()
    	temp = []
    	recursive(temp,0)
    	return result