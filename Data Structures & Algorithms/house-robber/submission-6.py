class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        rob1, rob2 = nums[0], max(nums[0], nums[1])
        i = 2
        while i < len(nums):
            newRob = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = newRob
            i += 1
        return rob2