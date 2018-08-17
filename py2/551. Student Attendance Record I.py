class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return not (s.count("A") > 1 or s.count("LLL") >= 1)

