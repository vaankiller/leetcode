class Solution(object):
    def arrangeCoins(self, n):
    """
    :type n: int
    :rtype: int
    """
    ret = 0
    coin_sum = 0
    i = 0
    while coin_sum + i + 1 <= n:
        ret += 1
        i += 1
        coin_sum += i
    return ret
