class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char = [0] * 26
        for c in s1:
            char[ord(c) - ord("a")] += 1
        l, r = 0, 0
        while r < len(s2):
            idx = ord(s2[r]) - ord("a")
            if char[idx] > 0:
                char[idx] -= 1
            else:
                while char[idx] == 0 and l < r:
                    char[ord(s2[l]) - ord("a")] += 1
                    l += 1
                if char[idx] > 0:
                    char[idx] -= 1
                else:
                    l = r + 1
            r += 1
            if r - l == len(s1):
                return True
        return False
                    
