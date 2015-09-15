class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = nums.size()
        r = n % k
        for i in range(r+1):
        	

        temp = nums[0]
        for i in range(k+1)
