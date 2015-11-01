class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        if s == None:
        	return result
        for i in range(len(s)-1):
        	if s[i:i+2] == "++":
        		temp = s[:i] + "--" + s[i+2:]
        		result.append(temp)
        return result