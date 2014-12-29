class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        h = {}
        for i in num:
        	if i in h:
        		continue
        	low = h[i-1] if i-1 in h else i
        	high = h[i+1] if i+1 in h else i
        	h[i] = i
        	h[low] = high
        	h[high] = low
        result = max(key-val+1 for key,val in h.iteritems())
        return result