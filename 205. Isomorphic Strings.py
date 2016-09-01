__author__ = 'vaan'


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "" and t == "":
            return True

        if len(s) != len(t):
            return False

        map = {}
        ret = []
        for idx in range(0, len(t)):
            i = s[idx]
            j = t[idx]
            if i not in map.keys() and j not in ret:
                map[i] = j
                ret.append(j)
            elif i in map.keys() and map[i] != j:
                return False
            elif j in ret and i not in map.keys():
                return False
        return True


s = Solution()
print s.isIsomorphic("add", "egg")