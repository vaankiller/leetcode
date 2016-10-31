__author__ = 'vaan'


class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        one_cnt = 0
        i = 1
        while i <= n:
            a = n / i  
            b = n % i  
            one_cnt += (a + 8) / 10 * i + (a % 10 == 1) * (b + 1)
            i *= 10
        return one_cnt


s = Solution()
print s.countDigitOne(13)
