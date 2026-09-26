class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost.append(0)
        dp = [cost[0], cost[1]]
        i = 2
        while i <= n:
            res = min(dp[0], dp[1])
            tmp = dp[1]
            dp[1] = res + cost[i]
            dp[0] = tmp
            i += 1
        return dp[1]       