class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[l] <= nums[m] and nums[r] < nums[l]:
                l = m + 1
            else:
                r = m
        cut = l
        l, r = 0, len(nums) - 1
        if target >= nums[cut] and target <= nums[r]:
            l = cut
        else:
            r = cut - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1