# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        gap = root.val - target
        while root:
        	if root.val == target:
        		return root.val
        	if abs(root.val - target) < abs(gap):
        		gap = root.val - target
        	if root.val < target:
        		root = root.right
        	else:
        		root = root.left
        return int(target + gap)
