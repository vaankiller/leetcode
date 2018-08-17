class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = "".join([i for i in s if i.isalpha() or i.isdigit()])
        for i in range(len(string)):
            if i < len(string)-i-1:
                if string[i].lower() != string[len(string)-i-1].lower():
                    return False 
        return True


s = Solution()
print s.isPalindrome("")