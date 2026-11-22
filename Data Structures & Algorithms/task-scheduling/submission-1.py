class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for t in tasks:
            if t not in freq:
                freq[t] = 0
            freq[t] += 1
        max_heap = []
        q = deque()
        t = 0
        for task in freq:
            heapq.heappush(max_heap, (-freq[task], task))
        while max_heap or q:
            if q and q[0][1] <= t:
                heapq.heappush(max_heap, (-freq[q[0][0]], q[0][0]))
                q.popleft()
            if max_heap:
                fq, task = heapq.heappop(max_heap)
                freq[task] -= 1
                if freq[task] > 0:
                    q.append((task, t + n + 1))
                t += 1
            else:
                t = q[0][1]
        return t