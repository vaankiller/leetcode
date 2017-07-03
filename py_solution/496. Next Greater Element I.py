class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    dic[nums[i]] = nums[j]
                    break
            else:
                dic[nums[i]] = -1
                
        return [dic[i] for i in findNums]
