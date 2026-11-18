class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        subset = []
        res = []
        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            skip = 1
            while i+skip < len(nums) and nums[i+skip] == nums[i]:
                skip += 1
            dfs(i+skip)
        dfs(0)
        return res