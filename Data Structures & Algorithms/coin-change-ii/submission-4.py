class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        # way to build 0 is 0
        for i in range(n):
            dp[i][0] = 1
        for i in range(n-1, -1, -1):
            for amt in range(1, amount + 1):
                dp[i][amt] = dp[i+1][amt]
                if amt - coins[i] >= 0:
                    dp[i][amt] += dp[i][amt-coins[i]]
        return dp[0][amount]