class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        val = self.timeMap[key]
        l, r = 0, len(val) - 1
        while l < r:
            m = (l + r + 1) // 2
            if val[m][1] <= timestamp:
                l = m
            else:
                r = m - 1
        if val[l][1] <= timestamp:
            return val[l][0]
        else:
            return ""
