class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [None]
        def distance(a, b):
            return math.sqrt(a ** 2 + b ** 2)
        def pop():
            heap[1] = heap.pop()
            i = 1
            while 2 * i < len(heap):
                if 2 * i + 1 < len(heap) and distance(heap[2 * i + 1][0], heap[2 * i + 1][1]) > distance(heap[2 * i][0], heap[2 * i][1]) and distance(heap[i][0], heap[i][1]) < distance(heap[2 * i + 1][0], heap[2 * i + 1][1]):
                    heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
                    i = 2 * i + 1
                elif distance(heap[i][0], heap[i][1]) < distance(heap[2 * i][0], heap[2 * i][1]):
                    heap[i], heap[2 * i] = heap[2 * i], heap[i]
                    i = 2 * i
                else:
                    break
        def add(x, y):
            heap.append((x, y))
            i = len(heap) - 1
            while i > 1 and distance(heap[i][0], heap[i][1]) > distance(heap[i // 2][0], heap[i // 2][1]):
                heap[i], heap[i // 2] = heap[i // 2], heap[i]
                i = i // 2
        for x, y in points:
            add(x, y)
        while len(heap) > k + 1:
            pop()
        return heap[1:]