from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def prod(i, nums):
            if len(nums) == 1:
                return nums[0] 
            elif i == 0:
                return nums[i] * nums[i + 1]
            elif i == len(nums) - 1:
                return nums[i - 1] * nums[i]
            return nums[i - 1] * nums[i] * nums[i + 1]
        maxTotal = 0
        @cache
        def dfs(nums):
            n = len(nums)
            if n == 1:
                return nums[0]
            else:
                total = max([prod(i, nums) + dfs(nums[:i] + nums[i+1:]) for i in range(len(nums))])
                return total
        return dfs(tuple(nums))
            
        '''
        1 2 3 4
        recursion:
            total(list) = max([prod(i) + total(list.remove(list[i]))] for i in range(len(list)))
        '''