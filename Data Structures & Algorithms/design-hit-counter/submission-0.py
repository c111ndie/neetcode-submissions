class HitCounter:

    def __init__(self):
        self.uniq_ts = []
        self.ts_cnt = defaultdict(int)
        
    def hit(self, timestamp: int) -> None:
        if not self.uniq_ts or (self.uniq_ts and self.uniq_ts[-1] != timestamp):
            self.uniq_ts.append(timestamp)
        self.ts_cnt[timestamp] += 1       

    def getHits(self, timestamp: int) -> int:
        start_time, end_time = timestamp - 300, timestamp
        hits = 0
        for ts in self.uniq_ts:
            if start_time < ts <= end_time:
                hits += self.ts_cnt[ts]
        return hits



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
