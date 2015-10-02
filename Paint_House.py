class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        f = [0]*3
        f_temp = [0]*3
        for i in range(n):
        	f_temp[0] = min(f[1],f[2]) + costs[i][0]
        	f_temp[1] = min(f[0],f[2]) + costs[i][1]
        	f_temp[2] = min(f[0],f[1]) + costs[i][2]
        	f = f_temp[:]
        return min(f)