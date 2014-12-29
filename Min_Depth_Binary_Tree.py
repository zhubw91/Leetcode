# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None:
        	return 0
        elif root.left is None and root.right is None:
        	return 1
        elif root.left is None:
        	return self.minDepth(root.right) + 1
        elif root.right is None:
        	return self.minDepth(root.left) + 1
        else:
        	return min(self.minDepth(root.right), self.minDepth(root.left)) + 1
        	