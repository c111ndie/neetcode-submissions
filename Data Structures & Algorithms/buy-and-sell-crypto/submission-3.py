class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) > 1:
            buy = prices[1]
        else:
            buy = 100
        for i in range(1, len(prices)):
            if buy > prices[i - 1]:
                buy = prices[i - 1]
            profit = max(profit, prices[i] - buy)
        return profit
            
        