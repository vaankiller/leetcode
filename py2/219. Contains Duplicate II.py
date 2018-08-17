class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i in range(0, len(nums) - k):
            if nums[i] in nums[i+1: i+k+1]:
                return True
        return False
    
