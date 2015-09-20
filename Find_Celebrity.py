# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        canditate = 0
        for i in range(1,n):
        	if knows(i,canditate) == False:
        		canditate = i

        for i in range(n):
        	if i == canditate:
        		continue
        	if knows(i,canditate) == False or knows(canditate,i) == True:
        		return -1
        return canditate