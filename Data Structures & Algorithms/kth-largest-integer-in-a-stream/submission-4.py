class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [None]
        for num in nums:
            self.heap.append(num)
            i = len(self.heap) - 1
            

            while i > 1 and self.heap[i] < self.heap[i // 2]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i // 2]
                self.heap[i // 2] = tmp
                i = i // 2
            while len(self.heap) > self.k + 1:
                self.pop(self.heap)
        
    def pop(self, heap):
        if len(heap) == 1:
            return None
        elif len(heap) == 2:
            return heap.pop()
        res = heap[1]
        heap[1] = heap.pop()
        i = 1
        while 2 * i < len(heap):
            if 2 * i + 1 < len(heap) and heap[2 * i + 1] < heap[2 * i] and heap[2 * i + 1] < heap[i]:
                tmp = heap[i]
                heap[i] = heap[2 * i + 1]
                heap[2 * i + 1] = tmp
                i = 2 * i + 1
            elif heap[2 * i] < heap[i]:
                tmp = heap[i]
                heap[i] = heap[2 * i]
                heap[2 * i] = tmp
                i = 2 * i 
            else:
                break
        return res

    def add(self, val: int) -> int:
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 1 and self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2
        while len(self.heap) > self.k + 1:
            self.pop(self.heap)
        return self.heap[1]
        
