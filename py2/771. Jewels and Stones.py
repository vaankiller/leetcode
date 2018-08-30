class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewel_cnt = 0
        for j in set(J):
            jewel_cnt += S.count(j)
        return jewel_cnt
