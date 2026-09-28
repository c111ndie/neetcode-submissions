from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i, t):
            if t == 0 and i == len(nums):
                return 1
            elif i == len(nums):
                return 0
            return dfs(i+1, t-nums[i]) + dfs(i+1, t+nums[i])
        return dfs(0, target)
        