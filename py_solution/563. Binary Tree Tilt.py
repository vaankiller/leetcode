# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        self.tilt = 0
        def _tilt(node):
            if not node: 
                return 0
            left, right = _tilt(node.left), _tilt(node.right)
            self.tilt += abs(left - right)
            return node.val + left + right
        _tilt(root)
        return self.tilt
    
