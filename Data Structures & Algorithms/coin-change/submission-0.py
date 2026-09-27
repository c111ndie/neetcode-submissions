class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        t = len(coins)
        coins.sort()
        if not coins:
            return -1
        if amount < min(coins) and amount != 0:
            return -1
        dp = [-1] * (amount + 1)
        i = 0
        dp[0] = 0
        while i <= amount:
            if i >= coins[0]:
                minCoin = float("inf")
                for j in range(t-1, -1, -1):
                    if coins[j] <= i:
                        if dp[i-coins[j]] != -1:
                            minCoin = min(dp[i-coins[j]] + 1, minCoin)
                if minCoin != float("inf"):
                    dp[i] = minCoin
            i += 1
        return dp[-1]


        