class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap = {}
        for c in s:
            if c not in charMap:
                charMap[c] = 1
            else:
                charMap[c] += 1

        for c in t:
            if c not in charMap:
                return False
            else:
                charMap[c] -= 1
        return all(val == 0 for val in charMap.values())