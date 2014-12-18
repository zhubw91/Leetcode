# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        stack = []
        result = []
        node = root
        while node != None or len(stack) > 0:
        	if node != None:
        		result.append(node.val)
        		stack.append(node)
        		node = node.left
        	else:
        		node = stack.pop()
        		node = node.right
        return result

