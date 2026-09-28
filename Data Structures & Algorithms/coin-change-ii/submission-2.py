class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}
        def cnt(i, amt):
            if amt == 0:
                return 1
            if i == len(coins) or amt < 0:
                return 0
            if (i, amt) in memo:
                return memo[(i, amt)]
            memo[(i, amt)] = cnt(i, amt-coins[i]) + cnt(i+1, amt)
            return memo[(i, amt)]
        return cnt(0, amount)
        