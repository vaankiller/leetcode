class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set([i for i in range(1, len(nums)+1)]) - set(nums))


def main():
    s = Solution()
    print s.findDisappearedNumbers([4,3,2,7,8,2,3,1])


if __name__ == '__main__':
    main()