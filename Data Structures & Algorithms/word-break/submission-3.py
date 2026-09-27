class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = len(wordDict)
        c_map = {}
        def check(s, i):
            if i == len(s):
                return True
            for j in range(m):
                word_len = len(wordDict[j])
                if s[i:i+word_len] == wordDict[j]:
                    if i+word_len not in c_map:
                        if not check(s, i+word_len):
                            continue
                        else:
                            return True
                    else:
                        if not c_map[i+word_len]:
                            continue
                        else:
                            return True
            c_map[i] = False
            return False
        return check(s, 0)
        

        