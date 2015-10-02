class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        l = len(nums)
        while i < l-1:
        	if nums[i] > nums[i+1]:
        		nums[i], nums[i+1] = nums[i+1], nums[i]
        	if i+2 < l and nums[i+1] < nums[i+2]:
        		nums[i+1], nums[i+2] = nums[i+2], nums[i+1]
        	i += 2
