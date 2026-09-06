class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = [''] * len(strs)
        str_map = {}
        res = []
        for i in range(len(strs)):
            sorted_strs[i] = ''.join(sorted(strs[i]))
            if sorted_strs[i] not in str_map:
                str_map[sorted_strs[i]] = [strs[i]]
            else:
                str_map[sorted_strs[i]].append(strs[i])
        for val in str_map.values():
            res.append(val)
        return res