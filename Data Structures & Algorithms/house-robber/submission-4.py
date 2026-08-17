class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def dfs(i):
            if i > len(nums) - 1:
                return 0
            elif cache[i] != -1:
                return cache[i]
            elif i == len(nums) - 1:
                cache[i] = nums[i]
                return nums[i]
            else:
                res = max(nums[i] + dfs(i + 2), dfs(i + 1))
                cache[i] = res
                return res
        return dfs(0)

        