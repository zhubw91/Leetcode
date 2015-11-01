import collections
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.hash = {}
        self.order = collections.deque()
        

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.hash:
            value = self.hash[key]
            self.order.remove(key)
            self.order.append(key)
            return value
        else:
            return -1
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.hash:
            old_value = self.hash[key]
            self.order.remove(key)
        if len(self.order) == self.cap:
            del self.hash[self.order[0]]
            self.order.popleft()
        self.order.append(key)
        self.hash[key] = value
