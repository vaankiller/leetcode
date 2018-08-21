"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        
        ret = []
        if root:
            current_level_q = [root]
        else:
            return ret
        
        while current_level_q:
            next_level_q = []
            level = []
            for node in current_level_q:
                level.append(node.val)
                next_level_q.extend(node.children)
            ret.append(level)
            current_level_q = next_level_q
        return ret
