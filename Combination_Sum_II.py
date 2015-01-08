class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        n = len(candidates)
        if n == 0:
        	return []
        candidates.sort()
        b = [0] * n
        can = [0] * n
        dup = 0
        last = -1
        for i in range(n):
        	if candidates[i] == last:
        		dup += 1
        		b[i-dup] += 1
        	else:
        		last = candidates[i]
        		can[i-dup] = last
        		b[i-dup] += 1
        n -= dup
        top = 0
        s = 0
        f = -1
        stack = []
        result = []
        while top >= 0:
    		if s == target:
    			temp = []
    			for i in range(top):
    				temp.append(can[stack[i]])
    			result.append(temp)
    			top -= 1
    			if top >= 0:
    				s -= can[stack[top]]
    				f = stack[top]
    				b[f] += 1
        	else:
        		f += 1
        		if f >= n or s > target:
        			top -= 1
        			if top >= 0:
        				s -= can[stack[top]]
        				f = stack[top]
        				b[f] += 1
        		elif b[f] > 0:
        			if top >= len(stack):
        				stack.append(f)
        			else:
        				stack[top] = f
        			b[f] -= 1
        			f -= 1
        			s += can[stack[top]]
        			top += 1
        return result


