class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = 1
        i = 0
        while i < len(nums):
        	if nums[i] != 0:
        		k = 1
        		i += 1
        	else:
        		if i + k >= len(nums):
        			break
        		elif nums[i+k] == 0:
        			k += 1
        		else:
        			nums[i], nums[i+k] = nums[i+k], nums[i]
        			i += 1
