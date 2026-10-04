class HitCounter:

    def __init__(self):
        self.uniq_ts = deque()
        self.ts_cnt = defaultdict(int)
        
    def hit(self, timestamp: int) -> None:
        if not self.uniq_ts or (self.uniq_ts and self.uniq_ts[-1] != timestamp):
            self.uniq_ts.append(timestamp)
            while self.uniq_ts[0] <= timestamp - 300:
                self.uniq_ts.popleft()
        self.ts_cnt[timestamp] += 1       

    def getHits(self, timestamp: int) -> int:
        hits = 0
        while self.uniq_ts and self.uniq_ts[0] <= timestamp - 300:
            self.uniq_ts.popleft()
        for ts in self.uniq_ts:
            hits += self.ts_cnt[ts]
        return hits



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
