class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        ret = []
        l = []

        for row in nums:
            l.extend(row)
        if len(l) != r*c:
            return nums
        else:
            for i in range(r):
                if i*c >= len(l):
                    break
                row = []
                for j in range(c):
                    if i*c+j >= len(l):
                        break
                    row.append(l[i*c+j])
                ret.append(row)
            return ret


def main():
    '''
    none
    '''
    s = Solution()
    ret = s.matrixReshape([[1,2],[3,4]], 2, 4)
    print ret

if __name__ == '__main__':
    main()
