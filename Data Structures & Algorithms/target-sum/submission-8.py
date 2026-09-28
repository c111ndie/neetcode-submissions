class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for n in nums:
            next_dp = defaultdict(int)
            for total, ways in dp.items():
                next_dp[total + n] += ways
                next_dp[total - n] += ways
            dp = next_dp
        return dp.get(target, 0)
        