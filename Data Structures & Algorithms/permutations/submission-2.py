class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        chosen = [False] * len(nums)
        res, p = [], []
        def dfs():
            if len(p) == len(chosen):
                res.append(p.copy())
                return
            for i in range(len(nums)):
                if not chosen[i]:
                    p.append(nums[i])
                    chosen[i] = True
                    dfs()
                    p.pop()
                    chosen[i] = False
        dfs()
        return res