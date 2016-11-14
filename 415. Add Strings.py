__author__ = 'vaan'


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ret = ""
        c = 0
        other = max(len(num1), len(num2)) - min(len(num1), len(num2))
        longer = num1 if len(num1) >= len(num2) else num2
        shorter = num1 if len(num1) < len(num2) else num2
        shorter = "0"*other + shorter
        for i, j in zip(longer[::-1], shorter[::-1]):
            total = (int(i) + int(j) + c)
            s = total % 10
            c = total / 10
            ret = str(s) + ret
        if c:
            ret = "1" + ret
        return ret


s = Solution()
print s.addStrings("0", "9")
