class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        maj = 0
        cnt = 0
        for item in num:
        	if cnt == 0:
        		maj = item
        		cnt = 1
        	else:
        		cnt = cnt + 1 if item == maj else cnt - 1
        return maj