class HitCounter:

    def __init__(self):
        self.uniq_ts = deque()
        self.ts_cnt = defaultdict(int)
        self.total_hits = 0 
        
    def hit(self, timestamp: int) -> None:
        if not self.uniq_ts or (self.uniq_ts and self.uniq_ts[-1] != timestamp):
            self.uniq_ts.append(timestamp)
            while self.uniq_ts[0] <= timestamp - 300:
                del_ts = self.uniq_ts.popleft()
                self.total_hits -= self.ts_cnt[del_ts]
                del self.ts_cnt[del_ts]
        self.ts_cnt[timestamp] += 1       
        self.total_hits += 1
    def getHits(self, timestamp: int) -> int:
        while self.uniq_ts and self.uniq_ts[0] <= timestamp - 300:
            del_ts = self.uniq_ts.popleft()
            self.total_hits -= self.ts_cnt[del_ts]
            del self.ts_cnt[del_ts]
        return self.total_hits



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
