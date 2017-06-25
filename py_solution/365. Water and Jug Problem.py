__author__ = 'vaan'


class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        return z == 0 or (x + y >= z and z % self.gcd(x, y) == 0)

    def gcd(self, x, y):
        return x if y == 0 else self.gcd(y, x % y)

s = Solution()
print s.canMeasureWater(0, 2, 1)

