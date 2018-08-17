class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        kinds = len(set(candies))
        maxmium = len(candies) / 2
        return kinds if kinds < maxmium else maxmium
        