__author__ = 'vaan'

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k <= 0 or nums is []:
            return []

        ret = []
        set_list = list(set(nums))
        feq_list = []
        for num in set_list:
            feq_list.append(nums.count(num))

        rank_list = sorted(feq_list, reverse=True)[:k]

        start = 0
        for i in range(k):
            if i == 0:
                ret.append(set_list[feq_list.index(rank_list[i])])
                start = feq_list.index(rank_list[i])
            else:
                if rank_list[i] == rank_list[i-1]:
                    ret.append(set_list[feq_list[start+1:].index(rank_list[i])+start+1])
                    start = feq_list[start+1:].index(rank_list[i])+start+1
                else:
                    ret.append(set_list[feq_list.index(rank_list[i])])
                    start = feq_list.index(rank_list[i])
        return ret




s = Solution()
s.topKFrequent([1,1,1,2,2,2,3,3,3], 3)