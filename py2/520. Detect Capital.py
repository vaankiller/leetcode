class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        if all(map(lambda x: x.isupper(), word)):
            return True
        elif all(map(lambda x: x.islower(), word)):
            return True
        elif word[0].isupper() and all(map(lambda x: x.islower(), word[1:])):
            return True
        else:
            return False

def main():
    s = Solution()
    print s.detectCapitalUse("flaG")

if __name__ == '__main__':
    main()
