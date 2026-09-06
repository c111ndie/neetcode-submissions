class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        new_str = "".join(res)
        return new_str

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while(s[j] != "#"):
                j += 1
            digit = int(s[i:j])
            res.append(s[j+1:j+1+digit])
            i = j+1+digit
        return res

