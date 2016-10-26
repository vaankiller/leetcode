__author__ = 'vaan'


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            rev = str(-x)[::-1]
            if -1*int(rev) < -1*2**31:
                return 0
            else:
                print -1*2**31
                return int(rev)*-1
        else:
            rev = str(x)[::-1]
            if int(rev) > 2**31-1:
                return 0
            else:
                return int(rev)


s = Solution()
print s.reverse(-2147483648)
