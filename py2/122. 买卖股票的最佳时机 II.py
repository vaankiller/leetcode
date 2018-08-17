class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total_profit = 0
        profits = []
        for i in range(1, len(prices)):
            profits.append(prices[i] - prices[i-1])
        
        for i in range(0, len(profits)):
            if profits[i] <= 0:
                continue
            else:
                total_profit += profits[i]
        return total_profit

