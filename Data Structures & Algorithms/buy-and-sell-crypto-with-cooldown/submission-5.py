class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in memo:
                return memo[(i, buy)]
            if buy == True:
                result = max(-prices[i] + dfs(i+1, False), dfs(i+1, buy))
            else:
                result = max(prices[i] + dfs(i+2, True), dfs(i+1, buy))
            memo[(i, buy)] = result
            return result
        return dfs(0, True)