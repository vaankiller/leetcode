__author__ = 'vaan'

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1:
        #     return 10
        #
        # ret = 9
        # for i in range(1,n):
        #     ret *= 10-i
        #
        # return self.countNumbersWithUniqueDigits(n-1)+ret
        if n == 0:
            return 1
        sum = 0
        for cnt in range(1, n+1):
            if cnt == 1:
                ret = 10
            else:
                ret = 9
            for i in range(1, cnt):
                ret *= 10-i
            sum += ret
        return sum

s = Solution()

print s.countNumbersWithUniqueDigits(1)