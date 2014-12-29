# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        def recursive(num, left, right):
        	if left > right:
        		return None
        	if left == right:
        		return TreeNode(num[left])
        	mid = (left + right)/2
        	result = TreeNode(num[mid])
        	result.left = recursive(num, left, mid - 1)
        	result.right = recursive(num, mid + 1, right)
        	return result
        if len(num) == 0:
        	return None
        return recursive(num, 0, len(num)-1)