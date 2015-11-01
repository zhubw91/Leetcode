import heapq
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        heights = []
        result = []
        q = [0]
        pre = 0
        for building in buildings:
        	l,r,h = building
        	heights.append((l,-h))
        	heights.append((r,h))
        heights.sort()
        print heights
        for height in heights:
        	index,h = height
        	if h < 0:
        		heapq.heappush(q,h)
        	else:
        		q.remove(-h)
        		print q
        	if len(q) > 0 and q[0] != pre:
        		pre = q[0]
        		result.append((index,-q[0]))
        return result
