class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        s = path.split("/")
        stack = []
        for x in s:
        	if x not in ["..",".",""]:
        		stack.append(x)
        	elif x == "..":
        		if stack:
        			stack.pop()
        result = ""
        for x in stack:
        	result += "/" + x
        if result == "":
        	result = "/"
        return result
