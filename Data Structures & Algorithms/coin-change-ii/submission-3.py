class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * n for _ in range(amount + 1)]
        dp[0] = [1] * n
        for amt in range(1, amount+1):
            if amt % coins[0] == 0:
                dp[amt][0] = 1
            for coin in range(1, n):
                if amt-coins[coin] >= 0:
                    dp[amt][coin] = dp[amt-coins[coin]][coin] + dp[amt][coin-1]
                else:
                    dp[amt][coin] = dp[amt][coin-1]
        return dp[amount][n - 1]