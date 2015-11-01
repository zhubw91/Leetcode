class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l == 0:
            return 
        k = k%l
        if k == 0:
            return 
        for i in range((l-k)/2):
            nums[i],nums[l-k-i-1] = nums[l-k-i-1],nums[i]
        for i in range(k/2):
            nums[l-k+i],nums[l-i-1] = nums[l-i-1],nums[l-k+i]
        for i in range(l/2):
            nums[i],nums[l-i-1] = nums[l-i-1],nums[i]

