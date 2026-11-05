class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = math.ceil(sum(piles) / h)
        r = max(piles)
        res = r
        while l < r:
            m = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)
            if hours > h:
                l = m + 1
            elif hours <= h:
                r = m
                res = min(m, res)
        return res 
            