__author__ = 'vaan'


class Solution1(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        re = []
        for i in self.generate(numRows-1):
            re.append(i)
        x = re[-1]
        new = [x[0]]
        for i in range(len(x)-1):
            new.append(x[i] + x[i+1])
        new.append(x[-1])
        re.append(new)
        return re


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        re = [[1]]
        for i in range(1, numRows):
            x1 = [0]+re[-1]
            x2 = re[-1]+[0]
            new = []
            for j in range(len(x1)):
                new.append(x1[j] + x2[j])
            re.append(new)
        return re

s = Solution()
s1 = Solution1()
print s.generate(5)
print s1.generate(5)