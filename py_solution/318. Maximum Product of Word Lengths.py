__author__ = 'vaan'


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # version one  Time Limit Exceeded
        # list = []
        # max = 0
        # for word in words:
        #     list.append(set(word))
        #
        # for i in range(len(list)):
        #     for j in range(i+1,len(list)):
        #         if not list[i] & list[j]:
        #             length = len(words[i]) * len(words[j])
        #             if length > max:
        #                 max = length
        # return max



s = Solution()
print s.maxProduct(["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"])
