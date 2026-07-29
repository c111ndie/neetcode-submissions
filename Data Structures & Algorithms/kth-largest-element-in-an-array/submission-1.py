class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num_amt = {}
        for num in nums:
            if num in num_amt.keys():
                num_amt[num] += 1
            else:
                num_amt[num] = 1
        num_amt = dict(sorted(num_amt.items()))
        k = len(nums) - k
        for key, val in num_amt.items():
            k -= val
            if k < 0:
                return key
            
        
        