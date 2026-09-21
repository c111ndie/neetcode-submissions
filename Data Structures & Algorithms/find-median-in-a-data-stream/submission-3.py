class MedianFinder:

    def __init__(self):
        self.first_half = []
        self.second_half = []

    def addNum(self, num: int) -> None:
        if not self.first_half:
            heapq.heappush(self.first_half, -num)
        elif len(self.first_half) > len(self.second_half) and -1 * self.first_half[0] <= num:
            heapq.heappush(self.second_half, num)
        elif len(self.first_half) > len(self.second_half) and -1 * self.first_half[0] > num:
            heapq.heappush(self.second_half, -1 * heapq.heappop(self.first_half))
            heapq.heappush(self.first_half, -num)
        else:
            if self.second_half[0] < num:
                heapq.heappush(self.first_half, -1 * heapq.heappop(self.second_half))
                heapq.heappush(self.second_half, num)
            else:
                heapq.heappush(self.first_half, -num)
            

    def findMedian(self) -> float:
        if not self.first_half and not self.second_half:
            return None
        if not self.second_half or len(self.first_half) > len(self.second_half):
            return -1 * self.first_half[0]
        else:
            return (-1 * self.first_half[0] + self.second_half[0]) / 2
        