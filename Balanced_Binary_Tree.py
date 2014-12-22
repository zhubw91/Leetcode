# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isbalancepart(self, root):
    	if root.left is None:
    		l = 0
    	else:
    		l = self.isbalancepart(root.left)
    	if root.right is None:
    		r = 0
    	else:
    		r = self.isbalancepart(root.right)
    	if l is -1 or r is -1 or abs(l-r) > 1:
    		return -1
    	else:
    		return max(l,r) + 1
    def isBalanced(self, root):
    	if root is None:
    		return True
    	result = self.isbalancepart(root)
    	if result is -1:
    		return False
    	else:
    		return True
        