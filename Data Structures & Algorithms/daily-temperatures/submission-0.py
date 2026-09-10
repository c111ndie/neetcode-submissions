class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmest = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while warmest and temperatures[warmest[-1]] < temperatures[i]:
                res[warmest[-1]] = i - warmest[-1]
                warmest.pop()
            warmest.append(i)
        return res

        