class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return filter(self._is_self_dividing_num, xrange(left, right+1))
    
    def _is_self_dividing_num(self, num):
        digits = [int(i) for i in str(num)]
        if 0 not in digits:
            for i in digits:
                if num % i:
                    break
            else:
                return True
        return False

