class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        
        if nums:
            ret = sum(sorted(nums)[::2])
        return ret
