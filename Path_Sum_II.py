# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
    	if root is None:
    		return None
    	queue = []
    	result = []
    	head = 0
    	tail = 1
    	queue.append([root,[],sum])
    	while head < tail:
    		if queue[head][0].right is None and queue[head][0].left is None:
    			if queue[head][2] == 0:
    				result.append(queue[head][1])
    		else:
    			if queue[head][0].left is not None:
    				temp = queue[head][1]
    				temp.append(queue[head][0].left.val)
    				queue.append([queue[head][0].left, temp, sum - queue[head][0].left.val])
    				tail = tail + 1
    			if queue[head][0].right is not None:
    				temp = queue[head][1]
    				temp.append(queue[head][0].right.val)
    				queue.append([queue[head][0].right, temp, sum - queue[head][0].right.val])
    				tail = tail + 1

    		head = head + 1
    	return result



        