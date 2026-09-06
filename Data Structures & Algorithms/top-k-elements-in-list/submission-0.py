class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        res = []
        for n in nums:
            freq[n] += 1
        for i in range(k):
            max_key = max(freq, key=freq.get)
            res.append(max_key)
            freq[max_key] = 0
        return res