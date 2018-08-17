# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def _convertBST(root):
            if root:
                _convertBST(root.right)
                root.val += self.add_up
                self.add_up = root.val
                _convertBST(root.left)        
        self.add_up = 0
        _convertBST(root)
        return root
