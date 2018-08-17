__author__ = 'vaan'


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0

        if grid and grid[0]:
            width, height = len(grid[0]), len(grid)
            for h in range(0, len(grid)):
                for w in range(0, len(grid[h])):
                    perimeter += self.side_count(grid, h, w, height, width) if grid[h][w] else 0
        return perimeter

    def side_count(self, grid, h, w, height, width):
        cnt = 0
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for move in moves:
            if 0 <= h+move[0] < height and 0 <= w+move[1] < width:
                if grid[h+move[0]][w+move[1]] == 0:
                    cnt += 1
            else:
                cnt += 1
        return cnt

s = Solution()
print s.islandPerimeter([[0,1,0,0],
                         [1,1,1,0],
                         [0,1,0,0],
                         [1,1,0,0]])

