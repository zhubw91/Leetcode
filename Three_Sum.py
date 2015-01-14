class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
    	targethash = {}
    	result = []
        for index,target in enumerate(num):
        	if targethash.has_key(target):
        		continue
        	targethash[target] = index
        	sumhash = {}
        	for i,item in enumerate(num):
        		if i == index:
        			continue
        		if item <= target and sumhash.has_key(-target-item) and sumhash[-target-item] == 1 and -target-item <= target:
        			if item < -target-item:
        				result.append([item,-target-item,target])
        			else:
        				result.append([-target-item,item,target])
        			sumhash[-target-item] = 0
        			sumhash[item] = 0
        		elif sumhash.has_key(-target-item) and sumhash[-target-item] == 0:
				    continue
        		else:
        			sumhash[item] = 1
        return result