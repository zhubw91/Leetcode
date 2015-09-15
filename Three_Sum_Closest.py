class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = sum(nums[:3])
        l = len(nums)
        for i in range(l):
        	top = i+1
        	tail = l-1
        	while top < tail:
        		s = nums[i] + nums[top] + nums[tail]
        		if abs(s-target) < abs(result-target):
        			result = s
        		if s < target:
        			top += 1
        		elif s > target:
        			tail -= 1
        		else:
        			return result
        return result

        