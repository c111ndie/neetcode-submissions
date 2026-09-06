class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if nums[i] == nums[i-1] and i > 0:
                continue
            j, k = i + 1, len(nums) - 1
            complement = nums[i] * -1
            while j < k:
                if nums[j] + nums[k] < complement:
                    j += 1
                elif nums[j] + nums[k] > complement:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
        return res
                

        