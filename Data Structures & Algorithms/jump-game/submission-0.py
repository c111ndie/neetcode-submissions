class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        i = len(nums) - 2
        while i >= 0:
            if nums[i] + i >= goal:
                goal = i
            i -= 1
        if goal == 0:
            return True
        return False