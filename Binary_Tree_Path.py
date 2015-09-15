# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        path_list = []
        path = ""
        stack = []
        stack_helper = []
        node = root
        if root == None:
        	return path_list
        stack.append(root)
        stack_helper.append(0)

        while len(stack) > 0:
        	node = stack[-1]
        	node_helper = stack_helper[-1]

        	if node.left != None and node_helper == 0:
        		stack.append(node.left)
        		stack_helper[-1] = 1
        		stack_helper.append(0)
        	elif node.right != None and node_helper <= 1:
        		stack.append(node.right)
        		stack_helper[-1] = 2
        		stack_helper.append(0)
        	elif node.left == None and node.right == None:
        		path = ""
        		for each_node in stack:
        			path += str(each_node.val) + "->"
        		path = path[:-2]
        		path_list.append(path)
        		stack.pop()
        		stack_helper.pop()
        	else:
        		stack.pop()
        		stack_helper.pop()

        return path_list
