__author__ = 'vaan'

unit = ["Zero ", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine "];
decade = ["Zero", "Ten", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "]
tenth = ["Ten ", "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "]
hundred = "Hundred "
thousand = "Thousand "
million = "Million "
billion = "Billion "

dct = {}
dct["unit"] = unit
dct["decade"] = decade
dct["tenth"] = tenth
dct[hundred] = 100
dct[thousand] = 1000
dct[million] = 1000000
dct[billion] = 1000000000
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret = self.pre(num)
        return ret[0:-1]

    def pre(self, num):
        ret = ""
        if num is None:
            return ret
        if num >= dct[billion]:
            ret += self.pre(num/dct[billion]) + billion + (self.pre(num % dct[billion]) if num % dct[billion] else "")
        elif num >= dct[million]:
            ret += self.pre(num/dct[million]) + million + (self.pre(num % dct[million]) if num % dct[million] else "")
        elif num >= dct[thousand]:
            ret += self.pre(num/dct[thousand]) + thousand + (self.pre(num % dct[thousand]) if num % dct[thousand] else "")
        elif num >= dct[hundred]:
            ret += self.pre(num/dct[hundred]) + hundred + (self.pre(num % dct[hundred]) if num % dct[hundred] else "")
        elif num >= 20:
            ret += dct["decade"][num/10] + (self.pre(num % 10) if num % 10 else "")
        elif num >= 10:
            ret += tenth[num % 10]
        else:
            ret += dct["unit"][num]
        return ret
s = Solution()
print s.numberToWords(2147891236)
print s.pre(2147891236)


