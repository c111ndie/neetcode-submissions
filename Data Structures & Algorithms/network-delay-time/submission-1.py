class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for s, node, w in times:
            adj[s].append((node, w))
        minHeap = [[0, k]]
        shortest = {}
        for i in range(1, n+1):
            shortest[i] = -1
        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if shortest[n1] == -1:
                shortest[n1] = t1
            else:
                continue
            for n2, t2 in adj[n1]:
                if shortest[n2] == -1:
                    heapq.heappush(minHeap, [t1 + t2, n2])
        if -1 in shortest.values():
            return -1
        else:
            return max(shortest.values())