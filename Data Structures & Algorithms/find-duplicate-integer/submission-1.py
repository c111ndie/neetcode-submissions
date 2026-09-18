class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow_2 = 0
        while slow_2 != slow:
            slow = nums[slow]
            slow_2 = nums[slow_2]
        return slow
