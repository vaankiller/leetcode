class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        for i in s.split(" "):
            if i == '':
                continue
            else:
                cnt += 1
        return cnt

