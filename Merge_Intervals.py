# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(lambda a,b:a.start-b.start)
        result = []
        pre = -1
        for i in range(len(intervals)):
        	if pre == -1:
        		result.append(intervals[i])
        		pre = 0
        	else:
        		if intervals[i].start <= result[pre].end:
        			result[pre].end = max(result[pre].end, intervals[i].end)
        		else:
        			result.append(intervals[i])
        			pre += 1
        return result

