# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left <= right:
        	if left == right:
        		if isBadVersion(left):
        			return left
        		else:
        			return -1
        	mid = (left+right)/2
        	if isBadVersion(mid):
        		right = mid
        	else:
        		left = mid+1
        
