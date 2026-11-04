class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_map = {}
        for s in strs:
            key = "".join(sorted(s))

            if key not in s_map:
                s_map[key] = []

            s_map[key].append(s)

        return list(s_map.values())