__author__ = 'vaan'


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str is None:
            return None

        sign = ('-', '+')
        nums = "0123456789"

        seq = list(str)
        for i in seq:
            if i == ' ':
                continue
            else:
                start = seq.index(i)
                break
        else:
            return 0

        if seq[start] in sign or seq[start] in nums:
            for i in seq[start+1:]:
                if i not in nums:
                    return int(''.join(seq[start+1:seq.index(i)]))
            else:
                return int(''.join(seq[start+1:]))
        else:
            return 0


s = Solution()
print s.myAtoi('     +')