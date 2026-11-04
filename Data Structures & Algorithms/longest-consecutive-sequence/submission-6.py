class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for n in nums_set:
            if n-1 not in nums_set:
                streak = 1
                for i in range(n+1, n+len(nums_set)):
                    if i in nums_set:
                        streak += 1
                    else:
                        break
                res = max(res, streak)
        return res