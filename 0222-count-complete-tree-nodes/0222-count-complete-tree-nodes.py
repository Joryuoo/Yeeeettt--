# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0

        left = right = 0

        # helper
        def depth(node):
            depth = 0
            while node:
                depth += 1
                node = node.left

            return depth

        l = depth(root.left)
        r = depth(root.right)


        if l == r:
            return (2 ** l) + self.countNodes(root.right)
        else:
            return (2 ** r) + self.countNodes(root.left)


        


            


        
       