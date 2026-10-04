class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def length(prev, i):
            if i == n:
                return 0
            if prev == -1 or nums[prev] < nums[i]:
                if (i, i+1) in memo:
                    result = max(length(prev, i+1), 1 + memo[(i, i+1)])
                else:
                    result = max(length(prev, i+1), 1 + length(i, i+1))
            else:
                result = length(prev, i+1)
            memo[(prev, i)] = result
            return result
        return length(-1, 0)


        