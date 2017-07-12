class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort = sorted(nums)
        return max(sort[-1]*sort[-2]*sort[-3], sort[-1]*sort[0]*sort[1])
