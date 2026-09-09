class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq1, freq2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            freq1[ord(s1[i]) - 97] += 1
        l, r = 0, len(s1) - 1
        for i in range(l, r + 1):
            freq2[ord(s2[i]) - 97] += 1
        while r < len(s2):
            if freq1 == freq2:
                return True
            else:
                freq2[ord(s2[l]) - 97] -= 1
                l += 1
                r += 1
                if r < len(s2): 
                    freq2[ord(s2[r]) - 97] += 1
        return False