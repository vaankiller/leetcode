import math


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        
        L = int(math.sqrt(area))
        
        if L * L == area:
            return [L, L]
        else:
            L += 1
            while divmod(area, L)[1]:
                L += 1
        return [L, area/L]

    def constructRectangle(self, area):
        mid = int(math.sqrt(area))
        while mid > 0:
            if area % mid == 0:
                return [int(area / mid), int(mid)]
            mid -= 1


def main():
    s = Solution()
    print s.constructRectangle(9999991)

if __name__ == '__main__':
    main()        
