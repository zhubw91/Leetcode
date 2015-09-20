class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        num_hash = {}
        num_hash['1'] = '1'
        num_hash['6'] = '9'
        num_hash['8'] = '8'
        num_hash['9'] = '6'
        num_hash['0'] = '0'
        i = 0
        j = len(num)-1
        while i<=j:
        	if i == j:
        		if num[i] == '1' or num[i] == '8' or num[i] == '0':
        			return True
        		else:
        			return False
        	elif num[i] in num_hash and num_hash[num[i]] == num[j]:
        		i += 1
        		j -= 1
        	else:
        		return False

        return True
