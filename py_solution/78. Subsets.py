__author__ = 'vaan'


class Solution(object):

    def dfs(self, start, S, result, father_subsets):
        result.append(father_subsets)
        for i in range(start, len(S)):
            self.dfs(i+1, S, result, father_subsets+[S[i]])


    def subsets(self, S):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if S is None:
            return []
        result = []
        self.dfs(0, sorted(S), result, [])
        return result


s = Solution()
print s.subsets([1, 2, 3])