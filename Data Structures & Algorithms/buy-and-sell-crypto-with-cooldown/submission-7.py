class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        can_buy, cant_buy = [0] * (len(prices) + 2), [0] * (len(prices) + 2)
        for i in range(len(prices)-1, -1, -1):
            can_buy[i] = max(-prices[i] + cant_buy[i+1], can_buy[i+1])
            cant_buy[i] = max(prices[i] + can_buy[i+2], cant_buy[i+1])
        return can_buy[0]
         