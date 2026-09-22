class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        subset = []
        def dfs(i):
            if sum(subset) == target:
                res.append(subset.copy())
                return
            elif i >= len(candidates) or sum(subset) > target:
                return
            subset.append(candidates[i])
            dfs(i + 1)
            subset.pop()
            skip = 1
            while i + skip < len(candidates) and candidates[i + skip] == candidates[i]:
                skip += 1
            dfs(i + skip)
        dfs(0)
        return res
        