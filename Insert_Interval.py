# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        result = []
        if len(intervals) == 0:
        	return [newInterval]
        pre = -1
        mark = -1
        for index,item in enumerate(intervals):
        	if newInterval.start > item.end or newInterval.end < item.start:
        		result.append(item)
        		if newInterval.start > item.end:
        			mark = index
        	else:
        		if pre == -1:
        			result.append(item)
        			pre = 1
        			result[-1].start = min(newInterval.start, result[-1].start)
        			result[-1].end = max(newInterval.end, result[-1].end)
        		else:
        			result[-1].end = max(result[-1].end, item.end)
        if pre == -1:
        	result.insert(mark+1,newInterval)

        return result