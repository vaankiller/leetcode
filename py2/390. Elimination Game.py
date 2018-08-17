__author__ = 'vaan'


class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
            
        res = 1
        left = n               
        interval = 1          
        from_left = True   
        while left > 1:            
            if from_left:
                res += interval
            else:
                if left % 2 == 0:
                    res = res
                else:
                    res += interval
            
            left /= 2
            interval *= 2
            from_left = not from_left
    
        return res