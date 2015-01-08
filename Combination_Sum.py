class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        n = len(candidates)
        if n == 0:
        	return []
        candidates.sort()
        top = 0
        s = 0
        f = -1
        stack = []
        result = []
        while top >= 0:
    		if s == target:
    			temp = []
    			for i in range(top):
    				temp.append(candidates[stack[i]])
    			result.append(temp)
    			top -= 1
    			if top >= 0:
    				s -= candidates[stack[top]]
    				f = stack[top]
        	else:
        		f += 1
        		if f >= n or s > target:
        			top -= 1
        			if top >= 0:
        				s -= candidates[stack[top]]
        				f = stack[top]
        		else:
        			if top >= len(stack):
        				stack.append(f)
        			else:
        				stack[top] = f
        			f -= 1
        			s += candidates[stack[top]]
        			top += 1
        return result


