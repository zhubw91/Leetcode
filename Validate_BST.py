# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        if root is None:
        	return True
        stack = []
        node = root
        pre = None
        while node != None or len(stack) > 0:
        	if node != None:
        		stack.append(node)
        		node = node.left
        	else:
        		node = stack.pop()
        		if pre != None and pre >= node.val:
        			return False
        		pre = node.val
        		node = node.right
        return True


