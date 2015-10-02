# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        result = 0
        while n>0:
        	tmpbuf = ['']*4
        	num = min(read4(tmpbuf),n)
        	for i in range(num):
        		buf[result+i] = tmpbuf[i]
        	result += num
        	n -= num
        	if num < 4:
        		break
        return result
