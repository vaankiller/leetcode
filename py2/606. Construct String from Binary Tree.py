# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        s = ""
        if t:
            s = str(t.val)
            if t.left:
                s += "(" + self.tree2str(t.left) + ")"
            if not t.left and t.right:
                s += "()"
            if t.right:
                s += "(" + self.tree2str(t.right) + ")"
        return s
