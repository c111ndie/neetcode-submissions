class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def count(i, amt):
            if amt == 0:
                return 1
            if i == 0:
                return 1 if not amt % coins[0] else 0
            if (i, amt) in memo:
                return memo[(i, amt)]
            coin = 0
            result = 0
            while coin <= amt:
                result += count(i-1, amt-coin)
                coin += coins[i]
            memo[(i, amt)] = result
            return result
        return count(len(coins) - 1, amount)
        