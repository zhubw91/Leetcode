# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root is None:
        	return None
        stack = [root]
        head = None
        while len(stack) > 0:
        	now = stack.pop()
        	if head is None:
        		head = root
        	else:
        		head.right = now
        		head.left = None
        	if now.right != None:
        		stack.append(now.right)
        	if now.left != None:
        		stack.append(now.left)
        	head = now
        head.right = None
        head.left = None
        return root
