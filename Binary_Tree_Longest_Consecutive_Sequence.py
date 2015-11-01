# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_l = 1
        def dfs(node,l,last,max_l):
        	if last != None and (last + 1) == node.val:
        		l += 1
        		max_l = max(l,max_l)
        	else:
        		l = 1
        	if node.left:
        		max_l = max(dfs(node.left,l,node.val,max_l),max_l)
        	if node.right:
        		max_l = max(dfs(node.right,l,node.val,max_l),max_l)
        	return max_l
        if root == None:
        	return 0
        max_l = dfs(root,0,None,max_l)
        return max_l