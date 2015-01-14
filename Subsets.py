def subsets(S):
    result = [[]]
    S.sort()
    for num in S:
    	for i in result:
    		if len(i) == 0 or i[-1] < num:
    			j = i[:]
    			j.append(num)
    			result.append(j)
    return result
print subsets([1,2,3])