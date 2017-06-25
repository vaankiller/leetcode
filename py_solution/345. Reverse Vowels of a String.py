__author__ = 'vaan'

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or "":
            return ""

        tmp = list(s)
        vowels = "aeiouAEIOU"

        i = 0
        j = len(tmp)-1
        while i < j:
            if tmp[i] not in vowels:
                i += 1
            else:
                if tmp[j] not in vowels:
                    j -= 1
                else:
                    tmp[i], tmp[j] = tmp[j], tmp[i]
                    i += 1
                    j -= 1
        return ''.join(tmp)

s = Solution()
print s.reverseVowels("leetcode")



