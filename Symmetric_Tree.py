# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        def check(node1, node2):
        	if node1 is None and node2 is None:
        		return True
        	if node1 is None or node2 is None:
        		return False
        	if node1.val == node2.val and check(node1.left, node2.right) and check(node1.right, node2.left):
        		return True
        	else:
        		return False
        if root is None:
        	return True
        return check(root.left, root.right)