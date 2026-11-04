class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("#")
            encoded.append(s)
        return "".join(encoded)


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        length = 0
        while i < len(s):
            if s[i] != "#":
                length = length * 10 + int(s[i])
                i += 1
            else:
                result.append(s[i+1:i+length+1])
                i = i + length + 1
                length = 0
        return result