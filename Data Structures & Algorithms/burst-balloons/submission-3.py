from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        @cache
        def dfs(l, r):
            if l > r:
                return 0
            result = 0
            for i in range(l, r + 1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dfs(l, i-1) + dfs(i+1, r)
                result = max(result, coins)
            return result
        return dfs(1, n)
        