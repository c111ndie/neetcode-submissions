class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [None]
        self.k = k
        for n in nums:
            self.heap.append(n)
            i = len(self.heap) - 1
            while i > 1 and self.heap[i] < self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
                i = i // 2
            while len(self.heap) > self.k + 1:
                self.pop()

    def pop(self):
        self.heap[1] = self.heap.pop()
        i = 1
        while 2 * i < len(self.heap): 
            if 2 * i + 1 < len(self.heap) and self.heap[2 * i] > self.heap[2 * i + 1] and self.heap[i] > self.heap[2 * i + 1]:
                self.heap[2 * i + 1], self.heap[i] = self.heap[i], self.heap[2 * i + 1]
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                self.heap[2 * i], self.heap[i] = self.heap[i], self.heap[2 * i]
                i = 2 * i
            else:
                break
        
            
    def add(self, val: int) -> int:
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2
        while len(self.heap) > self.k + 1:
            self.pop()
        return self.heap[1]
