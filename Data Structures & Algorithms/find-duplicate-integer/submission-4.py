class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while not slow == fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow2 = 0
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
        return slow2