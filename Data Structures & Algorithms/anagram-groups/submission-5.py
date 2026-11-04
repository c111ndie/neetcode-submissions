class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_map = {}
        for s in strs:
            freq = [0] * 26
            for char in s:
                freq[ord(char) - ord("a")] += 1
            key = tuple(freq)
            if key not in s_map:
                s_map[key] = []
            s_map[key].append(s)
        return list(s_map.values())