class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        start = 0
        end = 0
        n = len(gas)
        while start < n:
        	end = start
        	v = gas[start]
        	while end != start + n:
        		v -= cost[end%n]
        		if v < 0:
        			break
        		end += 1
        		v += gas[end%n]
        	if end == start + n:
        		return start
        	start = end + 1
        return -1
