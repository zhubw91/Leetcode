class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
        	return 0
        minsize = len(nums) + 1
        result = 0
        head = 0
        tail = 0
        while tail < len(nums):
        	result += nums[tail]
        	while result >= s and head <= tail:
        		minsize = min(minsize,tail-head+1)
        		result -= nums[head]
        		head += 1
        	tail += 1
        if minsize == len(nums) + 1:
        	minsize = 0
        return minsize