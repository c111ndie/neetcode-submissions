class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums)-2:
            target = -nums[i]
            pairs = self.twoSum(i+1, nums, target)
            if pairs:
                for pair in pairs:
                    pair.append(nums[i])
                    res.append(pair)
            i_tmp = nums[i]
            while nums[i] == i_tmp and i < len(nums)-2:
                i += 1
        return res
    
    def twoSum(self, j, nums, target):
        k = len(nums)-1
        res = []
        while j < k:
            if nums[j] + nums[k] < target:
                j += 1
            elif nums[j] + nums[k] > target:
                k -= 1
            else:
                res.append([nums[j], nums[k]])
                j_tmp, k_tmp = nums[j], nums[k]
                while nums[j] == j_tmp and j < k:
                    j += 1
                while nums[k] == k_tmp and j < k:
                    k -= 1
        return res