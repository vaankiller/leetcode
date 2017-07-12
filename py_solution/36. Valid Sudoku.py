__author__ = 'vaan'


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for str in board:
            for i in str:
                if i == '.':
                    continue
                elif i not in "123456789":
                    return False
                elif str.count(i) != 1:
                    return False

