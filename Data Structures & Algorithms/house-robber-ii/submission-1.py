class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        dp = [nums[0], max(nums[0], nums[1])]
        i = 3
        while i <= n - 1:
            tmp = dp[1]
            dp[1] = max(dp[0] + nums[i-1], dp[1])
            dp[0] = tmp
            i += 1
        first = dp[1]
        dp = [nums[1], max(nums[1], nums[2])]
        i = 4
        while i <= n:
            tmp = dp[1]
            dp[1] = max(dp[0] + nums[i-1], dp[1])
            dp[0] = tmp
            i += 1
        second = dp[1]
        return max(first, second)