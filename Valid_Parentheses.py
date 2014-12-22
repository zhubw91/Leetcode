class Solution:
    # @return a boolean
    def isValid(self, s):
        parstack = []
        for item in s:
        	if item is '(' or item is '[' or item is '{':
        		parstack.append(item)
        	else:
        		if len(parstack) is 0:
        			return False
        		current = parstack.pop()
        		if (current is '(' and item != ')') or (current is '[' and item != ']') or (current is '{' and item != '}'):
        			return False
        if len(parstack) > 0:
        	return False
        else:
        	return True
