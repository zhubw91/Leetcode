class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        result = []
        for i in range(len(input)):
        	if input[i] in ['+','-','*']:
        		result1 = self.diffWaysToCompute(input[:i])
        		result2 = self.diffWaysToCompute(input[i+1:])
        		for x in result1:
        			for y in result2:
        				if input[i] == '+':
        					result.append(x+y)
        				elif input[i] == '-':
        					result.append(x-y)
        				else:
        					result.append(x*y)
        if len(result) == 0:
        	result.append(int(input))
        return result