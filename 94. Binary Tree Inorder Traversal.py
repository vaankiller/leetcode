__author__ = 'vaan'

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if root is None:
            return ret

        if root.left is not None:
            ret += self.inorderTraversal(root.left)

        ret.append(root.val)

        if root.right is not None:
            ret += self.inorderTraversal(root.right)

        return ret
