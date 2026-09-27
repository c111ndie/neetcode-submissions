class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        for i in range(len(nums)):
            if nums[i] == target:
                return True
            next_dp = dp.copy()
            for j in dp:
                next_dp.add(j + nums[i])
                if j + nums[i] == target:
                    return True
            dp = next_dp.copy()
        if target not in dp:
            return False

        