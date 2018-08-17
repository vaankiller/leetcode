class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        l = map(lambda x: x[::-1], s.split(" "))
        return " ".join(l)
    
