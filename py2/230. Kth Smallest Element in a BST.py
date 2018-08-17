#! coding:utf:8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        if root is None:
            return None
        return self.serv(root)[k-1]

    def serv(self, root):
        if root is None:
            return None

        ser = []
        if root.left is not None:
            ser += self.serv(root.left)

        ser.append(root.val)

        if root.right is not None:
            ser += self.serv(root.right)
        print ser
        return ser

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val



lson = TreeNode(1)
rson = TreeNode(3)
root = TreeNode(2, right=rson, left=lson)
s = Solution()
print s.kthSmallest(root, 3)
