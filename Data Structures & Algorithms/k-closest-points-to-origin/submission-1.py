import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(point):
            return point[0] ** 2 + point[1] ** 2
        max_heap = [(-dist(point), point) for point in points]
        heapq.heapify(max_heap)
        while len(max_heap) > k:
            heapq.heappop(max_heap)
        res = []
        for i in range(len(max_heap)):
            res.append(max_heap[i][1])
        return res