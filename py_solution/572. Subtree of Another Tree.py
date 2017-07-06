# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_bintree(s, i):
    if s:
        node = TreeNode(s[i])
        if 2*i+1 < len(s) and s[2*i+1]:
            node.left = build_bintree(s, 2*i+1)
        if 2*i+2 < len(s) and s[2*i+2]:
            node.right = build_bintree(s, 2*i+2)
        return node

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        self.same_val_node = []
        def _find_val(root, x):
            if root:
                if root.val == x:
                    self.same_val_node.append(root)
                _find_val(root.left, x)
                _find_val(root.right, x)

        def _same_tree(s, t):
            if not s and not t:
                return True
            if s and t:
                if s.val == t.val:
                    return _same_tree(s.left, t.left) and _same_tree(s.right, t.right)
            return False

        if not s and not t:
            return True
        if s and t:
            _find_val(s, t.val)
            if self.same_val_node:
                return any(_same_tree(node, t) for node in self.same_val_node)
        return False


def main():
    s = Solution()
    src = build_bintree([3,4,5,1,2], 0)
    target = build_bintree([4,1,2], 0)
    print s.isSubtree(src, target)
    print s.isSubtree(build_bintree([1,1], 0), build_bintree([1], 0))


if __name__ == '__main__':
    main()