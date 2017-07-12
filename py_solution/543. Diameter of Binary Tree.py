# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        
        def _max_depth(node):
            left_depth = 0
            right_depth = 0
            
            if node.left:
                left_depth += _max_depth(node.left) + 1
            if node.right:
                right_depth += _max_depth(node.right) + 1
                
            if left_depth + right_depth > self.diameter:
                self.diameter = left_depth + right_depth
            return max(left_depth, right_depth)
        
        if root:
            _max_depth(root)
        return self.diameter