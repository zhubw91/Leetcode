class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 1
        high = len(nums) - 1
        while low < high:
        	mid = (low + high)/2
        	cnt = 0
        	for num in nums:
        		if num <= mid:
        			cnt += 1
        	if cnt <= mid:
        		low = mid + 1
        	else:
        		high = mid
        return low
