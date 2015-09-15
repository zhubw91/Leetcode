# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, value, result):
        	if node == None:
        		return result
        	if node.left == None and node.right == None:
        		return result + value*10 + node.val 
        	if node.left:
        		result = dfs(node.left, value*10 + node.val, result)
        	if node.right:
        		result = dfs(node.right, value*10 + node.val, result)
        	return result
        return dfs(root, 0, 0)