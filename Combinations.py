class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        result = []
        if k == 1:
        	for i in range(n):
        		result.append([i+1])
        else:
        	result = self.combine(n-1,k-1)
        	for item in result:
        		item.append(n)
        	if n > k:
        		result2 = self.combine(n-1,k)
        		for item in result2:
        			result.append(item)
        return result

