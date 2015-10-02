class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v = [v1,v2]
        self.index = [0,0] 
        self.current_list = 0
        self.n = 2
        

    def next(self):
        """
        :rtype: int
        """
        for i in range(self.n):
            k = (self.current_list + i)%self.n
            if self.index[k] < len(self.v[k]):
                result = self.v[k][self.index[k]]
                self.index[k] += 1
                self.current_list = (k+1)%self.n
                return result
        return None

    def hasNext(self):
        """
        :rtype: bool
        """
        for i in range(self.n):
            k = (self.current_list + i)%self.n
            if self.index[k] < len(self.v[k]):
                return True
        return False
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())