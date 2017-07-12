__author__ = 'vaan'


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        result, up = 1, None
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i] and (up is None or up is False):
                result += 1
                up = True
            elif nums[i - 1] > nums[i] and (up is None or up is True):
                result += 1
                up = False
        return result

s = Solution()
print s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])


