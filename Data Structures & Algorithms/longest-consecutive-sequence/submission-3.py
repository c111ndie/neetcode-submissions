class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums)
        res = 0
        for n in uniq:
            if n - 1 not in uniq:
                streak, cur = 0, n
                while cur in uniq:
                    streak += 1
                    cur += 1
                res = max(res, streak)
        return res
        