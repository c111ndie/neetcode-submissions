class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        sorted_freq = sorted(freq, key=freq.get, reverse=True)
        return sorted_freq[:k]