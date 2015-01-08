class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
        	return ''
        if len(strs) == 1:
        	return strs[0]
        n = len(strs)
        m = len(strs[0])
        flag = 0
        t = 0
        for i in range(m):
        	a = strs[0][i]
        	for j in range(1,n):
        		if len(strs[j]) <= i or strs[j][i] != a:
        			flag = 1
        			break
        	t = i
        	if flag == 1:
        		break
        if flag == 0:
        	t += 1
        return strs[0][:t]
