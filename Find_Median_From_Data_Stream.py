import heapq
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.heaps = [],[]
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        small, large = self.heaps
        heapq.heappush(large,num)
        heapq.heappush(small,-heapq.heappop(large))
        if len(small) > len(large)+1:
            heapq.heappush(large, -heapq.heappop(small))
        

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        small, large = self.heaps
        l1 = len(small)
        l2 = len(large)
        if l1 == 0:
            return None
        elif l1 == l2:
            return (-small[0] + large[0])/2.0
        else:
            return -small[0]

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()