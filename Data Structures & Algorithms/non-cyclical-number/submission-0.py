class Solution:
    def isHappy(self, n: int) -> bool:
        record = {}
        while True:
            squares_sum = 0
            num = n
            while num > 0:
                digit = num % 10
                squares_sum += digit * digit
                num //= 10
            if squares_sum in record:
                return False
            elif squares_sum == 1:
                return True
            record[n] = squares_sum
            n = squares_sum