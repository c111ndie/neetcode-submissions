from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, t):
            if t == 0 and i == len(nums):
                return 1
            elif i == len(nums):
                return 0
            if (i, t) in memo:
                return memo[(i, t)]
            memo[(i, t)] = dfs(i+1, t-nums[i]) + dfs(i+1, t+nums[i])
            return memo[(i, t)]
        return dfs(0, target)
        