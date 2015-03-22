class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
    	n = len(num)
    	flag = 0
    	last = 0
    	for index in range(n):
    		i = num[n-index-1]
    		if index == 0:
    			last = i
    			continue
    		if i < last:
    			num[n-index-1],num[n-index] = num[n-index],num[n-index-1]
    			j = n-index
    			while j < n-1 and num[j] < num[j+1]:
    				num[j],num[j+1] = num[j+1],num[j]
    				j += 1
    			flag = 1
    			break
    	if flag == 0:
    		num.reverse()
    	return num
