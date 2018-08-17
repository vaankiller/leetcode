

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permutations(nums):
            if not nums:
                yield []
            for n in nums:
                for p in permutations([i for i in nums if i != n]):
                    yield [n] + p

        return [p for p in permutations(nums)]


s = Solution()
print s.permute([1, 2, 3])
