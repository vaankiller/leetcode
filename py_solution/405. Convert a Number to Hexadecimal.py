__author__ = 'vaan'


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        return hex(num&0xFFFFFFFF)[2:]