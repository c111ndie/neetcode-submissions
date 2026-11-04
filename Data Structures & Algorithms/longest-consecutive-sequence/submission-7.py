class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for n in nums_set:
            if n-1 not in nums_set:
                streak = 1
                i = n+1
                while i in nums_set:
                    streak += 1
                    i += 1
                res = max(res, streak)
        return res