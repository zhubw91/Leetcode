class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        left = 0
        right = l-1
        leftmax,rightmax = 0,0
        result = 0
        while left <= right:
        	if height[left] <= height[right]:
        		leftmax = max(leftmax,height[left])
        		result += leftmax - height[left]
        		left += 1
        	else:
        		rightmax = max(rightmax,height[right])
        		result += rightmax - height[right]
        		right -= 1
        return result