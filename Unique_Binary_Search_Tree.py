# /**
#  * Taking 1~n as root respectively:
#  *      1 as root: # of trees = F(0) * F(n-1)  // F(0) == 1
#  *      2 as root: # of trees = F(1) * F(n-2) 
#  *      3 as root: # of trees = F(2) * F(n-3)
#  *      ...
#  *      n-1 as root: # of trees = F(n-2) * F(1)
#  *      n as root:   # of trees = F(n-1) * F(0)
#  *
#  * So, the formulation is:
#  *      F(n) = F(0) * F(n-1) + F(1) * F(n-2) + F(2) * F(n-3) + ... + F(n-2) * F(1) + F(n-1) * F(0)
#  */
class Solution:
    # @return an integer
    def numTrees(self, n):
    	f = [0] * (n+1)
    	f[0] = 1
    	for i in range(n+1):
    		for j  in range(i):
    			f[i] = f[i] + f[j]*f[i-j-1]
        return f[n]