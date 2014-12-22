class Solution:
    # @param num, a list of integer
    # @return an integer
    def subfind(self, num, start, end):
    	if start == end:
    		return start
    	elif start + 1 == end:
    		if num[start] > num[end]:
    			return start
    		else:
    			return end
    	else:
    		mid = (start + end)/2
    		if num[mid] > num[mid-1] and num[mid] > num[mid+1]:
    			return mid
    		elif num[mid] > num[mid-1] and num[mid+1] > num[mid]:
    			return self.subfind(num,mid+1,end)
    		else:
    			return self.subfind(num,start,mid-1)

    def findPeakElement(self, num):
        return self.subfind(num,0,len(num)-1)