__author__ = 'vaan'


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str is None:
            return None

        sign_tuple = ('-', '+')
        nums = "0123456789"

        sign = ''
        num = ''
        str = str.lstrip()
        if str:
            if str[0] in sign_tuple:
                sign = str[0]
                str = str[1:]
            for digit in str:
                if digit in nums:
                    num += digit
                else:
                    break
            if num == '':
                return 0
            else:
                if int(sign+num) > 2**31-1:
                    return 2**31-1
                elif int(sign+num) < -1*2**31:
                    return -1*2**31
                else:
                    return int(sign+num)
        else:
            return 0

s = Solution()
print s.myAtoi("2147483648")