# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
        	return False
        if root.left is None and root.right is None:
        	if root.val == sum:
        		return True
        	else:
        		return False
        if self.hasPathSum(root.left, sum - root.val) is False and self.hasPathSum(root.right, sum - root.val) is False:
        	return False
        else:
        	return True
