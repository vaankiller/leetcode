__author__ = 'vaan'

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        its = list(set(nums1) & set(nums2))
        ret = []

        for elem in its:
            if nums1.count(elem) > nums2.count(elem):
                cnt = nums2.count(elem)
            else:
                cnt = nums1.count(elem)

            for i in range(cnt):
                ret.append(elem)

        return ret

s = Solution()
print s.intersect([1, 2, 2, 1], [2, 2])



