class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if nums == None:
        	return ""
        nums = [str(x) for x in nums]
        nums.sort(cmp=lambda x,y: cmp(x+y,y+x), reverse=True)
        if nums[0] == '0':
        	return '0'
        else:
        	return ''.join(nums)