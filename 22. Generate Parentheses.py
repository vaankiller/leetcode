__author__ = 'vaan'

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        self.generate(n, n, '', ret)
        return ret


    def generate(self,left, right, s, ret):
        if left == 0 and right == 0:
            ret.append(s)
        if left > 0:
            self.generate(left-1, right, s+'(', ret)
        if right > 0 and left < right:
            self.generate(left, right-1, s+')', ret)


s = Solution()
print s.generateParenthesis(3)