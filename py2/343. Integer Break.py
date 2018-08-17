__author__ = 'vaan'

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        elif n == 2:
            return 1
        elif n == 3:
            return 2
        elif n == 4:
            return 4

        if n%3 ==0:
            return 3**(n/3)
        elif n%3 == 1:
            return 3**(n/3-1)*4
        else:
            return 3**(n/3)*2

s = Solution()
print s.integerBreak(9)