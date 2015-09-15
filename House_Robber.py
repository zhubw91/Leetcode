class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
        	return 0
        if n == 1:
        	return nums[0]
        light = [0] * n
        dark = [0] * n
        light[0] = nums[0]
        dark[0] = 0
        for i in range(1,n):
        	light[i] = dark[i-1] + nums[i]
        	dark[i] = max(dark[i-1],light[i-1])
        return max(light[n-1],dark[n-1])
