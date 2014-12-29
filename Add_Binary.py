class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        result = ''
        i = 0
        r = 0
        while i < len(a) and i < len(b):
        	j = len(a) - i - 1
        	k = len(b) - i - 1
        	result = str((int(a[j]) + int(b[k]) + r)%2) + result
        	r = (int(a[j]) + int(b[k]) + r)/2
        	i += 1
        while i < len(a):
        	j = len(a) - i - 1
        	result = str((int(a[j]) + r)%2) + result
        	r = (int(a[j]) + r)/2
        	i += 1
        while i < len(b):
        	k = len(b) - i - 1
        	result = str((int(b[k]) + r)%2) + result
        	r = (int(b[k]) + r)/2
        	i += 1
        if r > 0:
        	result = '1' + result
        return result
