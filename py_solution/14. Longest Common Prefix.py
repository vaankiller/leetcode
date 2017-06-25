__author__ = 'vaan'


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""

        if len(strs) == 1:
            return strs[0]

        min = len(strs[0])
        idx = 0
        for str in strs:
            s = len(str)
            if s < min:
                min = s
                idx = strs.index(str)

        for i in range(0, len(strs[idx])):
            for j in range(0, len(strs)):
                if strs[j][i] != strs[idx][i]:
                    return strs[idx][0:i]

        return strs[idx]


s = Solution()
print s.longestCommonPrefix(['aa', 'ab'])