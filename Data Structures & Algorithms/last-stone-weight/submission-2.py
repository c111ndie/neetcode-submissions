class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def heapify(l):
            l.append(l[0])
            cur = (len(l) - 1) // 2
            while cur > 0:
                i = cur
                while 2 * i < len(l):
                    if 2 * i + 1 < len(l) and l[i] < l[2 * i + 1] and l[2 * i + 1] > l[2 * i]:
                        l[i], l[2 * i + 1] = l[2 * i + 1], l[i]
                        i = 2 * i + 1
                    elif l[i] < l[2 * i]:
                        l[i], l[2 * i] = l[2 * i], l[i]
                        i = 2 * i
                    else:
                        break
                cur -= 1  
            return l
        def pop(heap):
            if len(heap) == 1:
                return None
            if len(heap) == 2:
                return heap.pop()
            res = heap[1] 
            heap[1] = heap.pop()
            i = 1
            while 2 * i < len(heap):
                if 2 * i + 1 < len(heap) and heap[i] < heap[2 * i + 1] and heap[2 * i + 1] > heap[2 * i]:
                    heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
                    i = 2 * i + 1
                elif heap[i] < heap[2 * i]:
                    heap[i], heap[2 * i] = heap[2 * i], heap[i]
                    i = 2 * i
                else:
                    break
            return res

        def push(heap, val):
            heap.append(val)
            i = len(heap) - 1
            while i > 1 and heap[i] > heap[i // 2]:
                heap[i], heap[i // 2] = heap[i // 2], heap[i]
                i = i // 2
            return heap

        stones = heapify(stones)
        while len(stones) > 1:
            if len(stones) == 2:
                return stones.pop()
            first = pop(stones)
            if first == stones[1]:
                pop(stones)
            elif first != stones[1]:
                second = pop(stones)
                push(stones, first - second)
        return 0
        

        
        


        