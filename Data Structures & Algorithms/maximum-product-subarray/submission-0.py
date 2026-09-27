class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd, maxProd, max_all = nums[0], nums[0], nums[0]
        for n in nums[1:]:
            next_max = max(n, maxProd*n, minProd*n)
            minProd = min(n, maxProd*n, minProd*n)
            maxProd = next_max
            max_all = max(max_all, maxProd)
        return max_all

        