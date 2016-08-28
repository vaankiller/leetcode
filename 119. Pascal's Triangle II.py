__author__ = 'vaan'


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        re = [[1]]
        for i in range(1, rowIndex+1):
            x1 = [0]+re[-1]
            x2 = re[-1]+[0]
            new = []
            for j in range(len(x1)):
                new.append(x1[j] + x2[j])
            re.append(new)
        return re[rowIndex]