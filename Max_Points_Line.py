# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        def gcd(a, b):
        	if a%b == 0:
        		return b
        	else:
        		return gcd(b, a%b)
        result = 0
        for i in range(len(points)):
        	line = {}
        	overlap = 0
        	ver = 0
        	hor = 0
        	tempmax = 0
        	for j in range(i+1,len(points)):
        		if points[i].x == points[j].x and points[i].y == points[j].y:
        			overlap += 1
        		else:
        			if points[i].x == points[j].x:
        				ver += 1
        			elif points[i].y == points[j].y:
        				hor += 1
        			else:
        				a = points[i].x - points[j].x
        				b = points[i].y - points[j].y
        				g = gcd(a,b)
        				a /= g
        				b /= g
        				if line.has_key((a,b)) is False:
        					line[(a,b)] = 1
        				else:
        					line[(a,b)] = line[(a,b)] + 1
        				tempmax = max(tempmax, line[(a,b)])
        	tempmax = max(tempmax, ver)
        	tempmax = max(tempmax, hor)
        	result = max(result, tempmax + overlap + 1)
        return result

