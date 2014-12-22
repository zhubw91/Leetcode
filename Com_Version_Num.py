class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        a = version1.split('.')
        b = version2.split('.')
        m = len(a)
        n = len(b)
        i = 0
        while i < m and i < n:
        	if string.atoi(a[i]) < string.atoi(b[i]):
        		return -1
        	elif string.atoi(a[i]) > string.atoi(b[i]):
        		return 1
        	else:
        		i = i + 1
        if i < m:
        	while i < m:
        		if string.atoi(a[i]) != 0:      # pay attention to '1.00.000.0' 
        			return 1
        		i = i + 1
        	return 0
        elif i < n:
        	while i < n:
        		if string.atoi(b[i]) != 0:
        			return -1
        		i = i + 1
        	return 0
        else:
        	return 0