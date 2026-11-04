class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, count in freq.items():
            buckets[count - 1].append(n)
        result = []
        for i in range(len(nums), -1, -1):
            for j in range(len(buckets[i])):
                if k <= 0:
                    break
                result.append(buckets[i][j])
                k -= 1
        return result