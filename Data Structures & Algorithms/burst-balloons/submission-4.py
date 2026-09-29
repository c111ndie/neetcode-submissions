class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (n+2) for _ in range(n+2)]
        for length in range(1, n+1):
            for l in range(1, n-length+2):
                r = l + length - 1
                for i in range(l, r+1):
                    coins = nums[l-1] * nums[i] * nums[r+1]
                    coins += dp[l][i-1] + dp[i+1][r]
                    dp[l][r] = max(dp[l][r], coins)
        return dp[1][n]