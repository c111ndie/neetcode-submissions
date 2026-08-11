class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        dp = [1, 2]
        i = 2
        while i < n:
            tmp = dp[1]
            dp[1] = tmp + dp[0]
            dp[0] = tmp
            i += 1
        return dp[1]
