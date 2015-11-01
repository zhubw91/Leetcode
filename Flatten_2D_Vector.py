class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.x = 0
        self.vec2d = vec2d
        while self.x < len(vec2d) and len(vec2d[self.x]) == 0:
            self.x += 1
        self.y = 0

    def next(self):
        """
        :rtype: int
        """
        result = self.vec2d[self.x][self.y]
        if self.y == len(self.vec2d[self.x])-1:
            self.x += 1
            self.y = 0
            while self.x < len(self.vec2d) and len(self.vec2d[self.x]) == 0:
                self.x += 1
        else:
            self.y += 1
        return result


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.x == len(self.vec2d):
            return False
        else:
            return True

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())