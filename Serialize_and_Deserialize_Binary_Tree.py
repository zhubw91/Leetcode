# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = [root]
        head = 0
        tail = 1
        result = []
        while head < tail:
            node = q[head]
            if node == None:
                result.append("null")
            else:
                result.append(node.val)
                q.append(node.left)
                q.append(node.right)
                tail += 2
            head += 1
        return ",".join(result)



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        s = data.split(",")
        head = 0
        tail = 1
        if s[0] == "null":
            return  None
        else:
            root = TreeNode(s[0])
        q = [root]
        i = 1
        while head < tail and i < len(s):
            node = q[head]
            if s[i] != "null":
                node.left = TreeNode(s[i])
                q.append(node.left)
                tail += 1
            if i+1<len(s) and s[i+1] != "null":
                node.right = TreeNode(s[i+1])
                q.append(node.right)
                tail += 1
            i += 2
            head += 1
        return root




        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))