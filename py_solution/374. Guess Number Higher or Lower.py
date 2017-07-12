__author__ = 'vaan'


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):


def guess(n):
    if n == 6:
        return 0
    if n > 6:
        return 1
    if n < 6:
        return -1

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        ret = guess((start+end)/2)

        while ret != 0:
            if ret == -1:
                start = (start+end)/2
            else:
                end = (end+start)/2
            ret = guess((start+end)/2)
        return (start+end)/2

s = Solution()
print s.guessNumber(10)