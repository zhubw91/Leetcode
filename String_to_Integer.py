class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        l = len(str)
        result = 0
        sign = 1
        state = 0
        intmax = 2147483647
        intmin = 2147483648
        for i in range(l):
        	if state == 0:
        		if str[i] == ' ':
        			continue
        		elif str[i] == '+' or str[i] == '-':
        			if str[i] == '-':
        				sign = -1
        			state = 1
        		elif str[i].isnumeric() == True:
        			result = int(str[i])
        			state = 1
        		else:
        			return 0
        	elif state == 1:
        		if str[i].isnumeric() == True:
        			if sign == 1 and (result > intmax/10 or intmax - result*10 < int(str[i])):
        				return intmax
        			elif sign == -1 and(result > intmin/10 or intmin - result*10 < int(str[i])):
        				return -1*intmin
        			else:
        				result = result*10 + int(str[i])
        		else:
        			return sign*result
        return sign*result




