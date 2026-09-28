class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in memo:
                return memo[(i, buy)]
            if buy == -1:
                result = max(dfs(i+1, i), dfs(i+1, buy))
            else:
                result = max(prices[i] - prices[buy] + dfs(i+2, -1), dfs(i+1, buy))
            memo[(i, buy)] = result
            return result
        return dfs(0, -1)