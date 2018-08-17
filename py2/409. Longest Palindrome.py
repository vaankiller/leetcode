class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        alpha_cnts = {alpha: s.count(alpha) for alpha in set(s)}
        odds = sum(cnt & 1 for cnt in alpha_cnts.values())
        return len(s) - odds + bool(odds)


s = Solution()
print s.longestPalindrome("aabbccdde")

