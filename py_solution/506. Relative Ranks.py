class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ret = []
        awarded = sorted(nums, reverse=True)
        
        for i in nums:
            if i == awarded[0]:
                ret.append("Gold Medal")
            elif len(awarded) >= 2 and i == awarded[1]:
                ret.append("Silver Medal")
            elif len(awarded) >= 3 and i == awarded[2]:
                ret.append("Bronze Medal")
            else:
                ret.append(str(awarded.index(i)+1))
        return ret


def main():
    s = Solution()
    ret = s.findRelativeRanks([5,4,3,2,1])
    print ret


if __name__ == '__main__':
    main()
