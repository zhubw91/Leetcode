class Solution:
    # @return an integer
    def maxArea(self, height):
        n = len(height)
        i = 0
        j = n-1
        result = 0
        while i < j:
        	result = max(result,(j-i)*min(height[i],height[j]))
        	if height[i] < height[j]:
        		i += 1
        	else:
        		j -= 1
        return result
