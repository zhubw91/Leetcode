class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.num_hash = {}
        

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number in self.num_hash:
            self.num_hash[number] += 1
        else:
            self.num_hash[number] = 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key in self.num_hash:
            num_hash = self.num_hash
            if value-key in num_hash and (value-key != key or num_hash[key]>1):
                return True
        return False
        

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)