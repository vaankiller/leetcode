__author__ = 'vaan'


class Solution:
    def getPermutation(self, n, k):
        numbers = range(1, n+1)
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            factorial = 1
            for i in range(1, n+1):
                factorial *= i
            index, k = divmod(k, factorial)
            permutation += str(numbers[index])
            numbers.remove(numbers[index])
        return permutation

s = Solution()
print s.getPermutation(3, 2)
