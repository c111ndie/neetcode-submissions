class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        val = set()
        for n in nums:
            if n in val:
                return True
            else:
                val.add(n)
        return False