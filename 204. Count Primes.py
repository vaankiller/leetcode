__author__ = 'vaan'

from math import sqrt


class Solution(object):
    def countPrimes1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0

        dic = [1, 0]
        for i in range(3, n+1):
            if i % 2 == 0:
                dic.append(1)
            else:
                dic.append(0)
        i = 2
        cnt = 0
        while i < n:
            if dic[i-1] == 0:
                cnt += 1
                k = 2
                while k*i < n:
                    if dic[k*i-1] == 0:
                        dic[k*i-1] = 1
                    k += 1

            i += 1
        return cnt

    def countPrimes2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0

        cnt = 0
        for i in range(1, n):
            if self.isPrime(i):
                cnt += 1
        return cnt

    def isPrime(self, n):
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True

        i = 2
        while i <= sqrt(n)+1:
            if n % i == 0:
                return False
            i += 1
        return True


    def countPrimes3(self, n):
        dic = [0] * (n + 1)
        count = 0

        for idx in range(2, n):
            if dic[idx] == 0:
                count += 1
                step = idx
                while step+idx < n:
                    step += idx
                    dic[step] = 1
        return count
s = Solution()
# print s.countPrimes1(1500000)
# print s.countPrimes2(1500000)

from timeit import Timer

t = Timer('s.countPrimes1(1500000)', 'from __main__ import s')
t2 = Timer('s.countPrimes3(1500000)', 'from __main__ import s')
print t.timeit(1)
print t2.timeit(1)

def countPrimes3(self, n):
    dic = [0] * (n + 1)
    count = 0

    for idx in range(2, n):
        if dic[idx] == 0:
            count += 1
            step = idx
            while step+idx < n:
                step += idx
                dic[step] = 1
    return count

