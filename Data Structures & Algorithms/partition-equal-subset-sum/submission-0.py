class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) / 2
        def dfs(i, res):
            if res == target:
                return True
            if i == len(nums):
                return False
            return dfs(i+1, res+nums[i]) or dfs(i+1, res)
        return dfs(0, 0)
        