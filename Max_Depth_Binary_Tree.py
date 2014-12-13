# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# @param root, a tree node
# @return an integer
def maxDepth(self, root):
	if root is None:
		return 0
	return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1