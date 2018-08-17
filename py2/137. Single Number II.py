__author__ = 'vaan'

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bitnum = []
        for x in range(32):
            bitnum.append(0)
        res = 0
        for i in range(32):
            for j in range(len(nums)):
                bitnum[i] += (nums[j] >> i) & 1
            res |= (bitnum[i] % 3) << i
        if res > 2**31-1:
            res -= 2**32
        return res
#
# int singleNumber(int* nums, int numsSize) {
#     int bitnum[32]={0};
#     int res=0;
#     for(int i=0; i<32; i++){
#         for(int j=0; j<numsSize; j++){
#             bitnum[i]+=(nums[j]>>i)&1;
#         }
#         res|=(bitnum[i]%3)<<i;
#     }
#     return res;
# }

s = Solution()
print s.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])