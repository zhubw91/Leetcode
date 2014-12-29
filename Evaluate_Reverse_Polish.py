class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        result = 0
        for item in tokens:
        	if str.isdigit(item) is True or ( item[0] == '-' and len(item) > 1):
        		stack.append(int(item))
        	else:
        		a = stack.pop()
        		b = stack.pop()
        		if item == '+':
        			result = a+b
        		if item == '-':
        			result = b-a
        		if item == '*':
        			result = a*b
        		if item == '/':
        			result = abs(b)/abs(a)
        			if a*b < 0:
        				result = result * -1
        		stack.append(result)
        result = stack.pop()
        return result



