__author__ = 'vaan'

from math import sqrt


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0

        map = []
        for i in range(1, n):
            map.append(0)

        map[0] = 1
        i = 2
        cnt = 0

        while i < n:
            if map[i-1] == 0:
                cnt += 1
                k = 2
                while k*i < n:
                    if map[k*i-1] == 0:
                        map[k*i-1] = 1
                    k += 1
            i += 1
        return cnt
















    # def countPrimes(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n < 0:
    #         return 0
    #
    #     cnt = 0
    #     for i in range(1, n):
    #         if self.isPrime(i):
    #             cnt += 1
    #     return cnt
    #
    # def isPrime(self, n):
    #     if n <= 1:
    #         return False
    #     if n == 2 or n == 3:
    #         return True
    #
    #     i = 2
    #     while i <= sqrt(n)+1:
    #         if n % i == 0:
    #             return False
    #         i += 1
    #     return True


s = Solution()
print s.countPrimes(1500000)