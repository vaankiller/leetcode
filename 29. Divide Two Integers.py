__author__ = 'vaan'


class Solution(object):
    def divide(self, dividend, divisor):
        if divisor == 0:
            return -1
        if dividend == 0:
            return 0

        ans, level,  = 0, abs(divisor)
        flag = dividend ^ divisor
        dic, table, dividend, divisor = {level: 1}, [level], abs(dividend), abs(divisor)

        for i in range(0, 31):
            dic[level + level], level = dic[level] + dic[level], level + level
            table.append(level)
        while dividend >= divisor:
            if level > dividend:
                level = table[table.index(level) - 1]
            else:
                dividend -= level
                ans += dic[level]
        if (ans > 2147483648) or (ans == 2147483648 and flag > 0):
            return 2147483647
        return -ans if flag < 0 else ans


s = Solution()
print s.divide(8, 3)
