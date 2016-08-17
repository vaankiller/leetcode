__author__ = 'vaan'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        ret = []
        d_ret = []
        father = []
        father.append(root)

        while father != []:
            tmp = []
            son = []
            for node in father:
                tmp.append(node.val)
                if node.left is not None:
                    son.append(node.left)
                if node.right is not None:
                    son.append(node.right)
            ret.append(tmp)
            father = son
        for i in ret[::-1]:
            d_ret.append(i)
        return d_ret

rs = TreeNode(7)
ls = TreeNode(15)
r = TreeNode(20, ls, rs)
l = TreeNode(9)
root = TreeNode(3, l, r)

s = Solution()
print s.levelOrderBottom(root)
