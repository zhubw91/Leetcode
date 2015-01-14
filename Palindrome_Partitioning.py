class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self,s):
        n = len(s)
        ispal = [[False for i in range(n)] for j in range(n)]
        result = [0]*(n+1)
        result[0] = [[]]
        for i in range(n):
    	    result[i+1] = []
    	    c = s[i]
    	
    	    for j in range(i+1):
    		    if j == i:
    			    ispal[i][i] = True
    		    else:
	    		    if s[j] != c:
	    			    continue
	    		    if j == i-1:
	    			    ispal[j][i] = True
	    		    else:
	    			    ispal[j][i] = ispal[j+1][i-1]
	    	    if ispal[j][i]:
	    		    for par in result[j]:
	    			    temp = par[:]
	    			    temp.append(s[j:i+1])
	    			    result[i+1].append(temp)
        return result[n]