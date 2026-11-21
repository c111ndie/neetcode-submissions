class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [None]
        def add(x):
            heap.append(x)
            i = len(heap) - 1
            while i > 1 and heap[i] > heap[i // 2]:
                heap[i], heap[i // 2] = heap[i // 2], heap[i]
                i = i // 2
        def pop():
            if len(heap) == 1:
                return None
            elif len(heap) == 2:
                return heap.pop()
            res = heap[1]
            heap[1] = heap.pop()
            i = 1
            while i * 2 < len(heap):
                if i * 2 + 1 < len(heap) and heap[i * 2 + 1] > heap[i * 2] and heap[i] < heap[i * 2 + 1]:
                    heap[i], heap[i * 2 + 1] = heap[i * 2 + 1], heap[i]
                    i = i * 2 + 1
                elif heap[i] < heap[i * 2]:
                    heap[i], heap[i * 2] = heap[i * 2], heap[i]
                    i = i * 2 
                else:
                    break
            return res
        if len(stones) == 1:
            return stones[0]
        elif len(stones) == 2:
            return abs(stones[0] - stones[1])
        for s in stones:
            add(s)
        while len(heap) > 2:
            x = pop()
            y = pop()
            if x == y:
                continue
            elif x > y:
                x, y = y, x
            add(y - x)
        if len(heap) == 2:
            return heap.pop()
        else:
            return 0

