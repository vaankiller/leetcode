__author__ = 'vaan'

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Memory Limit Exceeded
        # return max(map(sum, [nums[i: i+k] for i in range(len(nums)-k+1)])) / float(k)

        s = max_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            s += nums[i] - nums[i-k]
            if s > max_sum:
                max_sum = s
        return max_sum / float(k)

s = Solution()
print s.findMaxAverage([1, 12, -5, -6, 50, 3], 4)
print s.findMaxAverage([5], 1)
print s.findMaxAverage([0, 1, 1, 3, 3], 4)
print s.findMaxAverage([0, 4, 0, 3, 2], 1)
