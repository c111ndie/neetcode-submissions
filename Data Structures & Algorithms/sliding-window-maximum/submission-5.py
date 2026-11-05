class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        res = []
        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))
        res.append(-1 * max_heap[0][0])
        for i in range(k, len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))
            while max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            res.append(-1 * max_heap[0][0])
        return res