__author__ = 'vaan'


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a, base=2)
        b = int(b, base=2)

        return '{0:b}'.format(a+b)


s = Solution()
print s.addBinary('1110', '0111')
