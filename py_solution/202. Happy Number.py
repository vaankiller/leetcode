__author__ = 'vaan'


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        ret = []
        n = self.calculate(n)
        while n not in ret:
            print ret
            if n == 1:
                return True
            else:
                ret.append(n)
                n = self.calculate(n)
        return False


    def calculate(self, n):
        if n < 10:
            return n*n

        tmp = []
        while n >= 10:
            tmp.append(n%10)
            n /= 10
        tmp.append(n)
        return sum(x*x for x in tmp)

s = Solution()
print s.isHappy(123)
