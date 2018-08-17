class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x < 0:
            return self.mySqrt(-x)
        start = 1
        start = (x / start + start) / 2
        # TODO: Newton's method
         
    def mySqrt2(self, x):
        import math
        return int(math.sqrt(x))
