class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def ttlHours(n):
            ttl = 0
            for pile in piles:
                ttl += math.ceil(pile / n)
            return ttl
            
        l, r = 1, max(piles)
        res = 0
        while l <= r:
            m = (l + r) // 2
            if ttlHours(m) <= h:
                r = m - 1
                res = m
            elif ttlHours(m) > h:
                l = m + 1
        return res
            
        
        