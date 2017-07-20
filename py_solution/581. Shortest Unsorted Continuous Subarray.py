__author__ = 'vaan'

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # start, end = -1, len(nums)
        # for i in range(len(nums)):
        #     if i+1 < len(nums) and nums[i+1] < nums[i]:
        #         if i-1 > 0 and nums[i] != nums[i-1]:
        #             start = i
        #             break
        #         else:
        #             for k in range(i, -1, -1):
        #                 if nums[k] == nums[i]:
        #                     start = k
        #             break
        # for j in range(len(nums)-1, -1, -1):
        #     if j-1 >= 0 and nums[j] < nums[j-1]:
        #         if j+1 < len(nums) and nums[j] != nums[j+1]:
        #             end = j
        #             break
        #         else:
        #             for k in range(j, len(nums)):
        #                 if nums[k] == nums[j]:
        #                     end = k
        #             break
        # if start == -1 and end == len(nums):
        #     return 0
        # return end-start+1
        start, end = -1, len(nums)
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                start = i
                break
        for j in range(len(nums)-1, -1, -1):
            if nums[j] != sorted_nums[j]:
                end = j
                break
        if start == -1 and end == len(nums):
            return 0
        return end-start+1

s = Solution()
print s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
print s.findUnsortedSubarray([1, 2, 3, 4])
print s.findUnsortedSubarray([2, 1])
print s.findUnsortedSubarray([1, 3, 2, 2, 2])
