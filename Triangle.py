class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        f = []
        if len(triangle) == 1:
        	return triangle[0][0]
        f.append(triangle[0][0])
        for row in triangle:
        	if len(row) == 1:
        		continue
        	for i in range(len(row)):
        		t = len(row) - i - 1
        		if t == len(row) - 1:
        			f.append(f[t-1] + row[t])
        		elif t == 0:
        			f[t] = f[t] + row[t]
        		else:
        			f[t] = min(f[t],f[t-1]) + row[t]
        return min(f)

