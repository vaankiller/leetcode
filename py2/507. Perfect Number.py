class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num > 1:
            factors = self._find_factors(num)
            return sum(factors) == num
        else:
            return False
    
    def _find_factors(self, num):
        from math import sqrt
        factors = [1]
        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                factors.append(i)
                factors.append(num/i)
        return factors

