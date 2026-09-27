class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) / 2
        memo = {}
        def dfs(i, res):
            if res == target:
                memo[(i, res)] = True
                return True
            if i == len(nums):
                memo[(i, res)] = False
                return False
            if (i, res) in memo:
                return memo[(i, res)]
            return dfs(i+1, res+nums[i]) or dfs(i+1, res)
        return dfs(0, 0)
        