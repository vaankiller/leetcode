__author__ = 'vaan'


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True

        s = s.lower()
        str = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                str += i

        i = 0
        j = len(str)-1
        while i < j:
            if str[i] != str[j]:
                return False
            i += 1
            j -= 1

        return True


s = Solution()
print s.isPalindrome('a ba')