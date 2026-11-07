class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        values = self.time_map[key] 
        l, r = 0, len(values)
        while l < r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                l = m + 1
            else:
                r = m
        if not values or values[l - 1][1] > timestamp:
            return ""
        else:
            return values[l - 1][0]

