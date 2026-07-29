class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {target - num : i for i, num in enumerate(nums)}
        for i in range(len(nums)):
            if nums[i] in numMap and i != numMap[nums[i]]:
                return [i, numMap[nums[i]]]
            else:
                continue

        