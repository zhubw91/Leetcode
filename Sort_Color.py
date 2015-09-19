class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        a = 0
        b = 0
        c = n-1
        while b <= c:
        	if nums[b] == 0:
        		if a == b:
        			b += 1
        		else:
        			nums[a], nums[b] = nums[b], nums[a]
        	elif nums[b] == 2:
        		if b == c:
        			c -= 1
        		else:
        			nums[b], nums[c] = nums[c], nums[b]
        	else:
        		b += 1
        	if nums[a] == 0 and a < b:
        		a += 1
        	if nums[c] == 2:
        		c -= 1
