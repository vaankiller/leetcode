__author__ = 'vaan'

import copy

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        meta = copy.deepcopy(board)
        for i in board:
            print i
        if board == [[]]:
            return
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if meta[i][j] == 1:
                    if self.cnt_live(meta,i,j) < 2 or self.cnt_live(meta,i,j) > 3:
                        board[i][j] = 0
                        print i,j,":",self.cnt_live(meta,i,j), meta[i][j],"->",board[i][j]
                elif meta[i][j] == 0 and self.cnt_live(meta,i,j) == 3:
                    board[i][j] = 1
                    print i,j,":",self.cnt_live(meta,i,j), meta[i][j],"->",board[i][j]

    def cnt_live(self, board, i, j):
        cnt = 0
        imax = len(board)
        jmax = len(board[0])
        step = (-1, 0, 1)
        for i_move in step:
            for j_move in step:
                if i_move == 0 and j_move == 0:
                    continue
                elif i_move+i >= 0 and i_move + i < imax and j_move+j >= 0 and j_move +j < jmax:
                    if board[i_move+i][j_move+j] == 1:
                        cnt += 1
        return cnt


s = Solution()
print s.gameOfLife([[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]])
print s.cnt_live([[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]], 2, 2)

