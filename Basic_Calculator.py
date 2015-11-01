class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        current = 0
        op = '+'
        s += '+'
        for x in s:
        	if x in ['(',')',' ']:
        		continue
        	if x in ['+', '-']:
        		if op == '+':
        			result += current
        		else:
        			result -= current
        		current = 0
        		op = x
        	else:
        		current = current*10 + int(x)
        return result

