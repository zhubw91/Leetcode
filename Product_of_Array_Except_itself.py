class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        output = [1] * l
        left = 1
        right = 1
        for i in range(1,l):
        	left *= nums[i-1]
        	right *= nums[l-i]
        	output[i] *= left
        	output[l-i-1] *= right
        return output