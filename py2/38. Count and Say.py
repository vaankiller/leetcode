class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        else:
            seq = self.countAndSay(n-1)
            split_seq = self.split_seq(seq)
            return "".join([str(len(nums)) + str(nums[0]) for nums in split_seq])
                
            
    def split_seq(self, seq):
        ret = [[seq[0]], ]
        for num in seq[1:]:
            if num in ret[-1]:
                ret[-1].append(num)
            else:
                ret.append([num])
        return ret
