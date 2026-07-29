class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap = {}
        for c in s:
            if c in charMap:
                charMap[c] += 1
            else:
                charMap[c] = 1
        for c in t:
            if c in charMap and charMap[c] != 0:
                charMap[c] -= 1
            else:
                return False
        return all(val == 0 for val in charMap.values())