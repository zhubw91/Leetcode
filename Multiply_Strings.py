class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        l = l1+l2
        result = [0]*l
        for i in range(l1):
        	for j in range(l2):
        		result[i+j] += int(num1[l1-i-1])*int(num2[l2-j-1])
        r = 0
        t = 0
        for i in range(l):
        	t = (result[i]+r)/10
        	result[i] = (result[i]+r)%10
        	r = t
        if r > 0:
        	result.append(r)
        	l+=1
        num = ""
        flag = 0
        for i in range(l):
        	if flag == 0 and result[l-i-1] == 0:
        		continue
        	flag = 1
        	num += str(result[l-i-1])
        if num == "":
        	return "0"
        return num
