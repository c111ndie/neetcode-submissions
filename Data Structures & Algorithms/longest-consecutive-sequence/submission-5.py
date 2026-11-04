class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = []
        for i in range(len(nums)):
            subset = []
            if nums[i] - 1 not in nums_set:
                subset.append(nums[i])
                for j in range(nums[i]+1, nums[i]+len(nums)):
                    if j in nums_set:
                        subset.append(j)
                    else:
                        break
                if len(subset) > len(result):
                    result = subset
            else:
                continue
        return len(result)
        