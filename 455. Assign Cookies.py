__author__ = 'vaan'

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        n, m = len(g), len(s)
        i, j = 0, 0

        g = sorted(g)
        s = sorted(s)

        while i < n and j < m:
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i
