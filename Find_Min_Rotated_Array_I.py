class Solution:
    # @param num, a list of integer
    # @return an integer
    def findminpart(self, num, start, end):
    	if num[start] <= num[end]:
    		return num[start]
    	else:
    		mid = (start+end)/2
    		if num[start] > num[mid]:
    			return self.findminpart(num, start, mid)
    		else:
    			return self.findminpart(num, mid+1, end)
    	
    def findMin(self, num):
    	return self.findminpart(num, 0, len(num)-1)