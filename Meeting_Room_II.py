# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
        	return 0
        intervals.sort(key = lambda x: x.start)
        q = []
        heapq.heappush(q, intervals[0].end)
        for i in range(1, len(intervals)):
        	temp = heapq.heappop(q)
        	heapq.heappush(q, intervals[i].end)
        	if intervals[i].start < temp:
        		heapq.heappush(q, temp)
        return len(q)
