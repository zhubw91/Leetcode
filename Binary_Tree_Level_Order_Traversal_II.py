# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root is None:
        	return []
        result = []
        q = [(root,0)]
        top = 0
        tail = 1
        level = -1
        temp = []
        while top < tail:
        	if q[top][1] != level:
        		level = q[top][1]
        		if level != 0:
        			result.insert(0,temp)
        		temp = []
        		temp.append(q[top][0].val)
        	else:
        		temp.append(q[top][0].val)
        	now = q[top][0]
        	if now.left is not None:
        		q.append((now.left, q[top][1]+1))
        		tail += 1
        	if now.right is not None:
        		q.append((now.right, q[top][1]+1))
        		tail += 1
        	top += 1
        result.insert(0,temp)
        return result



