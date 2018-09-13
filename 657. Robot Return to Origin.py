class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        l_moves = moves.count("L")
        r_moves = moves.count("R")
        u_moves = moves.count("U")
        d_moves = moves.count("D")
        return l_moves == r_moves and u_moves == d_moves

