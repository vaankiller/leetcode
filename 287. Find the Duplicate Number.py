__author__ = 'vaan'

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return 0

        slow = 0
        slow = nums[slow]

        fast = 0
        fast = nums[nums[fast]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        find = 0
        while find != slow:
            slow = nums[slow]
            find = nums[find]
        return find

s = Solution()
print s.findDuplicate([1, 2, 2])