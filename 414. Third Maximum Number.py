__author__ = 'vaan'


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            nums = sorted(set(nums))
            return nums[len(nums)-1] if len(nums) < 3 else nums[-3]

s = Solution()
print s.thirdMax([1, 1, 2])


