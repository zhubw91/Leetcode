class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
    	if len(digits) == 0:
    		return ['']
        table ={'2':('a','b','c'),'3':('d','e','f'),'4':('g','h','i'),'5':('j','k','l'),'6':('m','n','o'),'7':('p','q','r','s'),'8':('t','u','v'),'9':('w','x','y','z')}
        result = []
        for num in digits:
        	if len(result) == 0:
        		for l in table[num]:
        			temp = ''
        			temp += l
        			result.append(temp)
        	else:
        		temp = result[:]
        		result = []
        		for l in table[num]:
        			for a in temp:
        				result.append(a+l)

        return result