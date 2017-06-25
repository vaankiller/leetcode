__author__ = 'vaan'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left_leaves = []
        sum = 0
        self.getLeftLeaves(root, left_leaves)

        for left_leaf in left_leaves:
            sum += left_leaf.val
        return sum


    def getLeftLeaves(self, root, left_leaves):
        if not root:
            return

        if root.left:
            if self.isLeaves(root.left):
                print root.left.val
                left_leaves.append(root.left)
            else:
                self.getLeftLeaves(root.left, left_leaves)

        if root.right:
            self.getLeftLeaves(root.right, left_leaves)


    def isLeaves(self, node):
        if not node:
            return
        if not node.left and not node.right:
            return True
        else:
            return False
