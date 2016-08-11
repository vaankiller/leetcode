__author__ = 'vaan'

import cmath
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # version 1 time limit exceed
        # if n == 0 or n == 1:
        #     return n
        #
        # bulbs = []
        # cnt = 0
        # for i in range(n):
        #     bulbs.append(0)
        #
        # for i in range(1, n+1):
        #     idx = i-1
        #     while idx < n:
        #         if bulbs[idx]:
        #             bulbs[idx] = 0
        #             cnt -= 1
        #         else:
        #             bulbs[idx] = 1
        #             cnt += 1
        #         idx += i
        # return cnt

        # version 2 只有在平方数的位置上的等是亮的
        return cmath.sqrt(n)

s = Solution()
print s.bulbSwitch(6)