class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        res = []
        res.append(max(nums[l:r+1]))
        while r < len(nums):
            if r + 1 < len(nums):
                if nums[l] == res[l] and nums[r + 1] < nums[l]:
                    res.append(max(nums[l+1:r+2]))
                elif nums[r + 1] > res[l]:
                    res.append(nums[r + 1])
                else:
                    res.append(res[l])
            l += 1
            r += 1
        return res
        