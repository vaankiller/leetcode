__author__ = 'vaan'

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        def is_square(n):
            import math
            root = int(math.sqrt(n))
            return root*root == n

        for i in range(int(c/2)+1):
            if is_square(i) and is_square(c-i):
                return True
        return False


s = Solution()
print s.judgeSquareSum(100000000)
