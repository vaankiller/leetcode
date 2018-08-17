__author__ = 'vaan'


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ret = []
        if words:
            qwer = "qwertyuiop"
            asd = "asdfghjkl"
            zxc = "zxcvbnm"
            alphabets = [qwer, asd, zxc]

            for word in words:
                for i in alphabets:
                    if all(map(lambda x: set(x.lower()).issubset(set(i)), word)):
                        ret.append(word)
        return ret


s = Solution()
print s.findWords(["Hello", "Alaska", "Dad", "Peace"])
